from django import forms
from Questionaire.models import Person

class PersonForm(forms.Form):
    last_name = forms.CharField(max_length=130)
    first_name = forms.CharField(max_length=130)
    email = forms.EmailField()
    address = forms.CharField(max_length=30)
    city = forms.CharField(max_length=30)
    state = forms.CharField(max_length=30)
    zip_code = forms.CharField(max_length=5)
    phone = forms.CharField(max_length=10)
