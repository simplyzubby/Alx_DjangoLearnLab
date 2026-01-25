from django import forms

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=100)
class SearchForm(forms.Form):
    q = forms.CharField(
        max_length=100,
        required=False
    )