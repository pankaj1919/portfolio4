from .models import *
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        widgets = {
            'description': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}),
        } 
        fields = '__all__'

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        widgets = {
            'service_des': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}),
        }
        fields = '__all__'

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class FactForm(forms.ModelForm):
    class Meta:
        model = Facts
        fields = '__all__'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        widgets = {
            'des': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}),
        }
        fields = '__all__'

        