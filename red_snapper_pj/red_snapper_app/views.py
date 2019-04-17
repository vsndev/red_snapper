from django.shortcuts import render
from django.http import HttpResponse
from .models import RegisterData
from .forms import RegisterForm
from django.shortcuts import redirect

# Create your views here.
def ShowLogin(request):
    return render(request, "login.html")


def ShowToppage(request):
    return render(request, "toppage.html")

def ShowRegister(request):

    if request.method == 'POST':
        model = RegisterData()
        register = RegisterForm(request.POST, instance = model)
        register.save()
        return redirect(to='/register')
    
    params = {
        'form': RegisterForm(),
    }
    return render(request,'register.html',params)