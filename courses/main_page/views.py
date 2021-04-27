import re
from django.shortcuts import render,redirect
from course.models import All_course,contact_form
from accounts.models import bkash
from django.contrib.auth.models import User
from django.db.models import Q
from django.template.loader import render_to_string
from django.http import JsonResponse


# Create your views here.


def home(request):
    courses=All_course.objects.all().order_by('-course_num')
    return render(request, "home.html", {'course':courses})



def contact(request):
    
    if request.method == 'POST':
        p = contact_form.objects.create(name=request.POST['username'],email=request.POST['email'],message=request.POST['summary'])
        p.save()
        return redirect('home')
    else:
        return render(request,"contact.html")