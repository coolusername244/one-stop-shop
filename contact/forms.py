from django import forms
from . import models


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = '__all__'
