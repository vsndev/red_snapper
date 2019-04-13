from django.shortcuts import render
from django.http.response import HttpResponse

def showlogin(request):
    return render(request, 'template_login.html')
