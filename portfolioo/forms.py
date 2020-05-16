from .models import *
from django import forms

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = portfolio
        fields = '__all__'

class PortfoliocategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'