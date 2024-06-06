from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from agency.models import Newspaper, Topic, Redactor


class NewspaperForm(forms.ModelForm):
    publisher = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Newspaper
        fields = "__all__"


class RedactorCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "years_of_experience",
        )


class RedactorUpdateForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = Redactor
        fields = (
            "first_name",
            "last_name",
            "years_of_experience",
        )
