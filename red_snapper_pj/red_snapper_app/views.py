from django.shortcuts import render
from django.http import HttpResponse
from .models import RegisterData
from .forms import RegisterForm
from django.shortcuts import redirect
import datetime

# Create your views here.
def ShowLogin(request):
    return render(request, "login.html")


def ShowToppage(request):
    today =datetime.date.today()
    borderdate = today + datetime.timedelta(weeks=1)
    data = RegisterData.objects.filter( deadline_date__lte = borderdate )

    if(RegisterData.objects.filter(deadline_date__isnull=True)):
        message = '提出期限がまずい人はいません。今はまだ。'

    else:
        message ='提出期限が迫ってます。リマインドしてあげてください。'

    params = {
        'data': data,
        'message': message,
    }
    return render(request, 'toppage.html', params)

def ShowRegister(request):
    data=RegisterData.objects.all()
    if request.method == 'POST':
        model = RegisterData()
        register = RegisterForm(request.POST, instance = model)
        register.save()
        return redirect(to='/register')
    
    params = {
        'form': RegisterForm(),
    }
    return render(request,'register.html',params)