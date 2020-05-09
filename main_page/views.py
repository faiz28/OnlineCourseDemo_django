from django.shortcuts import render
from course.models import All_course
# Create your views here.


def home(request):
    course=All_course.objects.all()
    return render(request,'home.html')