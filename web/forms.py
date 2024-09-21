from django import forms
from django.forms import widgets
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ("timestamp",)
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control big-input", 
                "placeholder": "First Name *"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control big-input", 
                "placeholder": "Email *"
            }),
            "mobil": forms.NumberInput(attrs={
                "class": "form-control big-input", 
                "placeholder": "Mobile *"
            }),
            "service": forms.TextInput(attrs={
                "class": "form-control big-input", 
                "placeholder": "Service *"
            }),
            "message": forms.Textarea(attrs={
                "class": "form-control big-input", 
                "placeholder": "Message *"
            }),
        }