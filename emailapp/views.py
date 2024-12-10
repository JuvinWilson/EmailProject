from django.shortcuts import render,redirect
from .models import User
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def add(request):
    return render(request,'Home.html')

def adddetails(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        pas=request.POST.get('pwd')
        obj=User(username=uname,email=email,password=pas)
        obj.save()
        subject="UserName and Password"
        message="Your username is "+str(uname)+" and your password is "+str(pas)
        recepient=request.POST.get('email')

        send_mail(subject,message,settings.EMAIL_HOST_USER,[recepient])
        return redirect('/')
    return render(request,'Home.html')