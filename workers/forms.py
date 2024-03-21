from django import forms
from .models import Registration

class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=10, required=True)
    last_name = forms.CharField(max_length=10, required=True)
    phone_no = forms.IntegerField()
    password = forms.CharField(max_length=20)


