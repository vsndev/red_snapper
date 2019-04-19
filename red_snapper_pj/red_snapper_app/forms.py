from django import forms
from django.forms import ModelForm, inlineformset_factory
from .models import RegisterData

class RegisterForm(forms.ModelForm):
    class  Meta:
        model = RegisterData
        fields = ["member_name","doc_title","deadline_date"]
        labels = {
            "member_name":"メンバー名",
            "doc_title":"提出書類",
            "deadline_date":"提出期限",
        }
        widgets = {
            "deadline_date": forms.SelectDateWidget
        }