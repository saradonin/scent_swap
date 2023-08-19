from django import forms
from django.contrib.auth.models import User


def validate_username_unique(value):
    if User.objects.filter(username=value):
        raise forms.ValidationError("Username is already taken")
