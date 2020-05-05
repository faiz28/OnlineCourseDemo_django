from django.shortcuts import render,get_object_or_404
from .models import Allcourse
# Create your views here.
def course(request):
    courses=Allcourse.objects.all()
    return render(request,'course/allcourse.html',{'courses':courses})
