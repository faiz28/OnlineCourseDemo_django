from django.shortcuts import render,get_object_or_404
from .models import All_course,All_lesson
from django.contrib.auth.decorators import login_required
from accounts.models import bkash
from django.db.models import Q


# Create your views here.
def course(request):
    courses=All_course.objects.all()
    return render(request,'course/allcourse.html',{'courses': courses})



@login_required(login_url="/accounts/signup")
def lesson(request,course_id):
    username = request.user.username
    obj=bkash.objects.filter(Q(username=username) & Q(permision=1) & Q(course_id=course_id))
    length= len(obj)
    if length>0:
       permit = 1
    else:
        permit = 0

    if permit==1:
        lesson = All_lesson.objects.all()
        detailcourse=get_object_or_404(All_course,pk=course_id)
        return render(request,'course/lesson.html',{'lesson':lesson,'course':detailcourse})
    else:
        return render(request,'course/detail.html',{'courses':detailcourse,'permit':permit})




def detail(request,course_id):
    detailcourse=get_object_or_404(All_course,pk=course_id)
    lesson=All_lesson.objects.all()
    username = request.user.username

    #Query from database
    play=bkash.objects.filter(Q(username=username) & Q(permision=1) & Q(course_id=course_id))
    pending= bkash.objects.filter(Q(username=username) & Q(permision=5) & Q(course_id=course_id))
    len_play= len(play)
    len_pending = len(pending)
    if len_play>0:
       permit = 1
    else:
        if len_pending>0:
            permit=5
        else:
            permit = 0
    return render(request,'course/detail.html',{'courses':detailcourse,'permit':permit,'lessons':lesson})

        