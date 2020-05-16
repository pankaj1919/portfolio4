from .models import *
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class EducationForm(forms.ModelForm):
    class Meta:
        model = resume_study
        widgets = {
            'des': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}),
        }
        fields = '__all__'

class WorkForm(forms.ModelForm):
    class Meta:
        model = work_history
        widgets = {
            'des': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}),
        }
        fields = '__all__'


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'

class TechnicalForm(forms.ModelForm):
    class Meta:
        model = Technical
        fields = '__all__'