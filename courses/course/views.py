from django.shortcuts import render,get_object_or_404,redirect
from .models import All_course,All_lesson,Review,course_details,ki_ki_sikhben
from django.contrib.auth.decorators import login_required
from accounts.models import bkash
from django.db.models import Q
from django.http import JsonResponse


# Create your views here.
def course(request):
    courses=All_course.objects.all().order_by('-course_num')
    return render(request,'course/allcourse.html',{'courses': courses})



@login_required(login_url="/accounts/signup")
def lesson(request,course_id):
    username = request.user.username
    obj=bkash.objects.filter(Q(username=username) & Q(permision=1) & Q(course_id=course_id))
    length= len(obj)
    
    lesson = All_lesson.objects.all()
    detailcourse=get_object_or_404(All_course,pk=course_id)
  
    return render(request,'course/lesson.html',{'lesson':lesson,'courses':detailcourse})
   



def detail(request,course_id):
    detailcourse=get_object_or_404(All_course,pk=course_id)
    review = Review.objects.all().order_by('-id')
    lesson=All_lesson.objects.all()
    username = request.user.username


    play=bkash.objects.filter(Q(username=username) & Q(permision=1) & Q(course_id=course_id))
    pending= bkash.objects.filter(Q(username=username) & Q(permision=5) & Q(course_id=course_id))
    free=All_course.objects.filter(Q(pk=course_id) & Q(price=0))
    len_play= len(play)
    len_pending = len(pending)
    free_len=len(free)

    if detailcourse.price!=0:
            price=1
    else: 
        price = 0

    #Course Details find here
    detail=course_details.objects.filter(Q(course_num=detailcourse.course_num))
    ki_sikhben=ki_ki_sikhben.objects.filter(Q(course_num=detailcourse.course_num))



    if detailcourse.course_num==1:
        var = 1
    else:
        var = 0

    if len_play>0:
       permit = 1
    else:
        if len_pending>0:
            permit=5
        else:
            permit = 0
    
    if free_len==1:
        permit=1
    
    if request.method == 'POST' and (permit==1  or var == 1 ):
            Review_data = Review.objects.create(username=username,course_id=course_id,summary=request.POST['summary'],ratting=request.POST['rating'])
            Review_data.save()
            return render(request,'course/allcourse.html',{'courses':detailcourse,'permit':permit,'lessons':lesson,'var':var,'review':review,'course_id':course_id,'price':price}) 
    else:
        return render(request,'course/detail.html',{'courses':detailcourse,'permit':permit,'lessons':lesson,'var':var,'review':review,'course_id':course_id,'price':price,'pen':len_pending,'len':len_play,'free':free_len,'detail':detail,'ki_ki_sikhben':ki_sikhben})





