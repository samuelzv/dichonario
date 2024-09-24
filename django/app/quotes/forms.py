from django.forms import ModelForm, widgets
from .models import Quote
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class QuoteForm(ModelForm):

    class Meta:
        model = Quote
        fields = ["quote", "author", "is_private"]
        widgets = {
            "quote": widgets.Textarea(attrs={"cols": 60, "rows": 4}),
        }


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
