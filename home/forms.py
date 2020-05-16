from .models import *
from django import forms
from django.contrib.auth.models import User

class HomeForm(forms.ModelForm):

    class Meta:
        model = Home
        fields = '__all__'

