from django import forms
from django.contrib.auth.models import User


def validate_username_unique(value):
    """
    Validate whether username is unique
    """
    if User.objects.filter(username=value):
        raise forms.ValidationError("Username is already taken")


def validate_perfume_volume(value):
    """
    Validate whether volume value if positive
    """
    if not isinstance(value, int):
        raise forms.ValidationError("Volume value must be integer")
    if value < 0:
        raise forms.ValidationError("Volume value must be a positive number")
    if value > 5000:
        raise forms.ValidationError("That's absurd amount of perfume")
