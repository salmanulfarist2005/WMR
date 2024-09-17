from django import forms
from django.forms import widgets
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ("timestamp",)
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "First Name *"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Last Name*"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email *"}),
            "mobil": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Mobile *"}),
            "street_address": forms.TextInput(attrs={"class": "form-control", "placeholder": "Street Address *"}),
            "pincode": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Pincode *"}),
            "state": forms.TextInput(attrs={"class": "form-control", "placeholder": "State *"}),
            "city": forms.TextInput(attrs={"class": "form-control", "placeholder": "City *"}),       
         }
