from django.forms import ModelForm
from .models import *
from django.db import models
from django import forms

class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = '__all__'
		exclude=['user']
		widgets = {'image': forms.FileInput}

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email', 'username']
