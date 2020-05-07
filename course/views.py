from django.shortcuts import render,get_object_or_404
from .models import Allcourse
# Create your views here.
def course(request):
    courses=Allcourse.objects.all()
    return render(request,'course/allcourse.html',{'courses':courses})

def detail(request,course_id):
    detailblog=get_object_or_404(Allcourse,pk=course_id)
    return render(request,'course/detail.html',{'courses':detailblog})
