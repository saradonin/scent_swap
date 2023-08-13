from django import forms


class SearchForm(forms.Form):
    value = forms.CharField(label="",
                            max_length=32,
                            widget=forms.TextInput(attrs={'placeholder': 'Search',
                                                          'class': 'form-control bg-secondary text-white',
                                                          'style': 'width: 160px;'}))
