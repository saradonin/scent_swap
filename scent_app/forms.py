from django import forms


class SearchForm(forms.Form):
    value = forms.CharField(label="",
                            max_length=32,
                            widget=forms.TextInput(attrs={'placeholder': 'Search',
                                                          'class': 'form-control bg-secondary text-white',
                                                          'style': 'width: 160px;'}))


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64, widget=forms.PasswordInput)
