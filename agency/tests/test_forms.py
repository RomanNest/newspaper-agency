from django.test import TestCase

from agency.forms import RedactorCreationForm, RedactorSearchForm, NewspaperSearchForm, TopicSearchForm


class FormTest(TestCase):
    def test_redactor_creation_form_with_years_of_experience(self):
        form_date = {
            "username": "new_user",
            "password1": "user12test",
            "password2": "user12test",
            "first_name": "Test_first",
            "last_name": "Test_last",
            "years_of_experience": 3,
        }
        form = RedactorCreationForm(data=form_date)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_date)
        self.assertTrue(form.is_valid())


class RedactorSearchFormTest(TestCase):
    def test_renew_form_username_max_length(self):
        form = RedactorSearchForm()
        self.assertTrue(
            form.fields["username"].max_length == 255
        )

    def test_renew_form_username_required(self):
        form = RedactorSearchForm()
        self.assertTrue(
            form.fields["username"].required is False
        )

    def test_renew_form_username_label(self):
        form = RedactorSearchForm()
        self.assertTrue(
            form.fields["username"].label == ""
        )

    def test_renew_form_username_widget(self):
        form = RedactorSearchForm()
        self.assertTrue(
            form.fields["username"].widget.attrs["placeholder"]
            == "Search by username"
        )


class NewspaperSearchFormTest(TestCase):
    def test_renew_form_title_max_length(self):
        form = NewspaperSearchForm()
        self.assertTrue(
            form.fields["title"].max_length == 255
        )

    def test_renew_form_title_required(self):
        form = NewspaperSearchForm()
        self.assertTrue(
            form.fields["title"].required is False
        )

    def test_renew_form_title_label(self):
        form = NewspaperSearchForm()
        self.assertTrue(
            form.fields["title"].label == ""
        )

    def test_renew_form_title_widget(self):
        form = NewspaperSearchForm()
        self.assertTrue(
            form.fields["title"].widget.attrs["placeholder"]
            == "Search by title"
        )


class TopicSearchFormTest(TestCase):
    def test_renew_form_name_max_length(self):
        form = TopicSearchForm()
        self.assertTrue(
            form.fields["name"].max_length == 255
        )

    def test_renew_form_name_required(self):
        form = TopicSearchForm()
        self.assertTrue(
            form.fields["name"].required is False
        )

    def test_renew_form_name_label(self):
        form = TopicSearchForm()
        self.assertTrue(
            form.fields["name"].label == ""
        )

    def test_renew_form_name_widget(self):
        form = TopicSearchForm()
        self.assertTrue(
            form.fields["name"].widget.attrs["placeholder"]
            == "Search by name"
        )
