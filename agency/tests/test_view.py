import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from agency.models import Topic, Newspaper

TOPIC_URL = reverse("agency:topic_list")
NEWSPAPER_URL = reverse("agency:newspaper_list")
REDACTOR_URL = reverse("agency:redactor_list")


class PublishViewsTest(TestCase):
    def test_topic_login_required(self):
        res = self.client.get(TOPIC_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_newspaper_login_required(self):
        res = self.client.get(NEWSPAPER_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_redactor_login_required(self):
        res = self.client.get(REDACTOR_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivetViewsTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123",
            years_of_experience=20,
        )
        self.client.force_login(self.user)

    def test_topic_retrieve_list(self):
        Topic.objects.create(name="test")
        Topic.objects.create(name="test1")
        res = self.client.get(TOPIC_URL)
        topics = Topic.objects.all()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            list(res.context["topic_list"]),
            list(topics)
        )
        self.assertTemplateUsed(res, "agency/topic_list.html")

    def test_newspaper_retrieve_list(self):
        topic = Topic.objects.create(name="test")
        Newspaper.objects.create(
            title="title_test",
            content="content_test",
            published_date=datetime.datetime.now(),
            topic=topic
        )
        Newspaper.objects.create(
            title="title_test1",
            content="content_test1",
            published_date=datetime.datetime.now(),
            topic=topic
        )
        res = self.client.get(NEWSPAPER_URL)
        newspapers = Newspaper.objects.all()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            list(res.context["newspaper_list"]),
            list(newspapers)
        )
        self.assertTemplateUsed(res, "agency/newspaper_list.html")

    def test_newspaper_detail(self):
        topic = Topic.objects.create(name="test")
        Newspaper.objects.create(
            title="title_test",
            content="content_test",
            published_date=datetime.datetime.now(),
            topic=topic
        )
        res = self.client.get(reverse("agency:newspaper_detail", kwargs={"pk": 1}))
        self.assertEqual(res.status_code, 200)

    def test_redactor_retrieve_list(self):
        get_user_model().objects.create_user(
            username="test_0",
            password="test523",
            years_of_experience=10
        )
        get_user_model().objects.create_user(
            username="test_1",
            password="test234",
            years_of_experience=6,
        )
        res = self.client.get(REDACTOR_URL)
        redactors = get_user_model().objects.all()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            list(res.context["redactor_list"]),
            list(redactors)
        )
        self.assertTemplateUsed(res, "agency/redactor_list.html")

    def test_redactor_detail(self):
        get_user_model().objects.create_user(
            username="test_0",
            password="test523",
            years_of_experience=10,
        )
        res = self.client.get(reverse("agency:redactor_detail", kwargs={"pk": 1}))
        self.assertEqual(res.status_code, 200)
