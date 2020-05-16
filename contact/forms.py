from .models import *
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'