from django.shortcuts import render

# Create your views here.
def ShowLogin(request):
    return render(request, "login.html")
