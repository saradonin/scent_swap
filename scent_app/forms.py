from django import forms
from django.core.validators import validate_email

from scent_app.models import UserPerfume, Perfume
from scent_app.validators import validate_username_unique, validate_perfume_volume


class SearchForm(forms.Form):
    """
    Form for searching by value.

    Attributes:
        value (str): The search value, limited to 32 characters.
    """
    value = forms.CharField(label="",
                            max_length=32,
                            widget=forms.TextInput(attrs={'placeholder': 'Search',
                                                          'class': 'form-control bg-secondary text-white'}))


class UserLoginForm(forms.Form):
    """
    Form for user login.

    Attributes:
        username (str): The username of the user, limited to 64 characters.
        password (str): The password of the user.
    """
    username = forms.CharField(max_length=64,
                               widget=forms.TextInput(attrs={'class': 'form-control bg-secondary text-white'}))
    password = forms.CharField(max_length=64,
                               widget=forms.PasswordInput(attrs={'class': 'form-control bg-secondary text-white'}))


class UserAddForm(forms.Form):
    """
    Form for adding a new user.

    Attributes:
        username (str): The username of the new user, limited to 64 characters.
        email (str): The email address of the new user, limited to 64 characters.
        password1 (str): The password of the new user.
        password2 (str): The repeated password for confirmation.
    """
    username = forms.CharField(max_length=64, validators=[validate_username_unique],
                               widget=forms.TextInput(attrs={'class': 'form-control bg-secondary text-white'}))
    email = forms.CharField(max_length=64, validators=[validate_email],
                            widget=forms.TextInput(attrs={'class': 'form-control bg-secondary text-white'}))
    password1 = forms.CharField(max_length=64, label="Password:",
                                widget=forms.PasswordInput(attrs={'class': 'form-control bg-secondary text-white'}))
    password2 = forms.CharField(max_length=64, label="Repeat password:",
                                widget=forms.PasswordInput(attrs={'class': 'form-control bg-secondary text-white'}))

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


class UserPerfumeAddForm(forms.Form):
    """
    Form for adding a perfume to user's collection.

    Attributes:
        volume (IntegerField): The volume of the perfume.
        status (CharField): The status of the perfume in the user's collection.
        to_exchange (BooleanField): Whether the user is open to exchanging the perfume.
    """
    volume = forms.IntegerField(required=False, validators=[validate_perfume_volume])
    status = forms.CharField(required=False, max_length=255)
    to_exchange = forms.BooleanField(required=False)


class OfferAddForm(forms.Form):
    """
    Form for adding a new swap offer
    """
    offering_perfume = forms.ModelChoiceField(
        queryset=None,
        widget=forms.Select(attrs={'class': 'form-control bg-secondary text-white'})
    )

    requested_perfume = forms.ModelChoiceField(
        queryset=Perfume.objects.all().order_by("brand", "name"),
        widget=forms.Select(attrs={'class': 'form-control bg-secondary text-white'})
    )

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Limit choices for offering_perfume field to UserPerfume objects owned by the logged-in user
        self.fields['offering_perfume'].queryset = UserPerfume.objects.filter(user=user).order_by("perfume__brand",
                                                                                                  "perfume__name")


class MessageAddForm(forms.Form):
    """
    Form for creating and sending a message to another user
    """
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control bg-secondary text-white',
        'rows': 3,
    }))
