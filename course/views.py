from django.shortcuts import render,get_object_or_404
from .models import All_course,All_lesson
from django.contrib.auth.decorators import login_required


# Create your views here.
def course(request):
    courses=All_course.objects.all()
    return render(request,'course/allcourse.html',{'courses': courses})

def detail(request,course_id):
    detailcourse=get_object_or_404(All_course,pk=course_id)
    return render(request,'course/detail.html',{'courses':detailcourse})

@login_required(login_url="/accounts/signup")
def lesson(request,course_id):
    lesson = All_lesson.objects.all()
    detailcourse=get_object_or_404(All_course,pk=course_id)
    return render(request,'course/lesson.html',{'lesson':lesson,'course':detailcourse})
