from django import forms
from django.contrib.auth.models import User


def validate_username_unique(value):
    """
    Validate whether username is unique
    """
    if User.objects.filter(username=value):
        raise forms.ValidationError("Username is already taken")
