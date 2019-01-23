from django import forms

from .models import Contact

class ContactForm(forms.ModelForm):
    first_name  = forms.CharField(label='',
                    widget=forms.TextInput(attrs={"placeholder": "First Name"}))

    last_name  = forms.CharField(label='',
                    widget=forms.TextInput(attrs={"placeholder": "Last Name"}))

    phone_number  = forms.CharField(label='',
                    widget=forms.TextInput(attrs={"placeholder": "Phone Number"}))

    email  = forms.CharField(label='',
                    widget=forms.TextInput(attrs={"placeholder": "Email"}))




    class Meta:
        model = Contact
        fields =[
            'first_name',
            'last_name',
            'phone_number',
            'email',
        ]



class RawContactForm(forms.Form):
    first_name   = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "First Name"}))
    last_name    = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Last Name"}))
    phone_number = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Phone Number"}))
    email        = forms.EmailField(label='', widget=forms.TextInput(attrs={"placeholder": "Email"}))
