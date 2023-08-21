from django import forms
from django.core.validators import validate_email

from scent_app.validators import validate_username_unique


class SearchForm(forms.Form):
    value = forms.CharField(label="",
                            max_length=32,
                            widget=forms.TextInput(attrs={'placeholder': 'Search',
                                                          'class': 'form-control bg-secondary text-white'}))


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64, widget=forms.PasswordInput)


class UserAddForm(forms.Form):
    """
    Form for adding a new user.

    Attributes:
        username (str): The username of the new user, limited to 64 characters.
        email (str): The email address of the new user, limited to 64 characters.
        password1 (str): The password of the new user.
        password2 (str): The repeated password for confirmation.
    """
    username = forms.CharField(max_length=64, validators=[validate_username_unique])
    email = forms.CharField(max_length=64, validators=[validate_email])
    password1 = forms.CharField(max_length=64, label="Password:", widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=64, label="Repeat password:", widget=forms.PasswordInput)

    def clean(self):
        """
        Clean and validate the form data.

        Raises:
            forms.ValidationError: If the passwords do not match.
        """
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError('Passwords are not the same!')

