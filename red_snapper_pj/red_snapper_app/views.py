from django.shortcuts import render
from django.http import HttpResponse
#from django.views.generic import CreateView
#from django.views.generic.edit import CreateView
from .models import RegisterData
from .forms import RegisterForm
from django.shortcuts import redirect

# Create your views here.
def ShowLogin(request):
    return render(request, "login.html")


def ShowToppage(request):
    return render(request, "toppage.html")

#削除予定
#class CreateRegisterView(CreateView):
    #model = RegisterData
    #form_class = RegisterForm
    #template_name = 'register.html'
    #success_url = "/"

def ShowRegister(request):

    if request.method == 'POST':
        model = RegisterData()
        register = RegisterForm(request.POST, instance = model)
        register.save()
        return redirect(to='/register')
    
    #検証用削除予定
    params = {
        'title': 'Guten Morgen',
        'form': RegisterForm(),
    }
    return render(request,'register.html',params)