from django import forms
from django.forms import ModelForm, inlineformset_factory
from .models import RegisterData

class RegisterForm(forms.ModelForm):
    class  Meta:
        model = RegisterData
        fields = ("member_name","doc_title","deadline_date")