from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import bkash

# Create your views here.

def register(request):
    if request.method == 'POST':
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request,'accounts/signup.html',{'error':'Username already exit'})
            except User.DoesNotExist:
                user=User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password1'], first_name=request.POST['first_name'], last_name=request.POST['last_name'])
                user.save()
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request,'accounts/signup.html',{'error':'Password Does not match'})
    else:
        return render(request,'accounts/signup.html')
def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'accounts/signin.html',{'error':'username or password is incorrect.'})
    else:
        return render(request,'accounts/signin.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

def bkash_from(request):
    if request.method == 'POST':
        p = bkash.objects.create(username=request.POST['username'],email=request.POST['email'],mobile_number=request.POST['number'],transaction_id=request.POST['id'])
        p.save()
        return redirect('course')
    else:
        return render(request,'accounts/bKash_payment.html')
