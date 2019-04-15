from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import RegisterData
from .forms import RegisterForm


# Create your views here.
def ShowLogin(request):
    return render(request, "login.html")


def ShowToppage(request):
    return render(request, "toppage.html")


class CreateRegisterView(CreateView):
    model = RegisterData
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = "/"
