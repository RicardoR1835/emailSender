from multiprocessing import context
from urllib import response
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail



def index(request):
    return render(request, "mcemails/index.html")

def create(request):
    if request.method =="POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                return redirect('/')
        user = User.objects.create(first_name=request.POST["fn"], last_name=request.POST["ln"], email=request.POST["email"], password=request.POST["password"])
        request.session['id'] = user.id

        subject = 'welcome to User Dash'
        message = f'Hi {user.first_name}, thank you for registering. This will be your primary email account: {user.email}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email ]
        send_mail( subject, message, email_from, recipient_list )
        return redirect('/dash')
        
def dash(request):
    return render(request, "mcemails/dash.html")





