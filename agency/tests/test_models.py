import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase

from agency.models import Topic, Newspaper


class ModelTests(TestCase):
    def test_topic_str(self):
        topic = Topic.objects.create(name="test")
        self.assertEqual(str(topic), f"{topic.name}")

    def test_newspaper_str(self):
        topic = Topic.objects.create(name="test")
        newspaper = Newspaper.objects.create(
            title="test_title",
            content="test_content",
            published_date=datetime.datetime.today().date(),
            topic=topic,
        )
        self.assertEqual(str(newspaper.title), newspaper.title)

    def test_redactor_str(self):
        redactor = get_user_model().objects.create(
            username="test",
            password="test123",
            first_name="First_test",
            last_name="Last_test",
        )
        self.assertEqual(
            str(redactor),
            f"{redactor.username} "
            f"({redactor.first_name} {redactor.last_name})"
        )

    def test_redactor_with_years_of_experience(self):
        username = "test"
        password = "test123"
        years_of_experience = 20
        redactor = get_user_model().objects.create_user(
            username=username,
            password=password,
            years_of_experience=years_of_experience,
        )
        self.assertEqual(redactor.username, username)
        self.assertEqual(redactor.years_of_experience, years_of_experience)
        self.assertTrue(redactor.check_password(password))
