from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.course,name='course'),
    path('<int:course_id>/',views.detail,name='detail'),
]
