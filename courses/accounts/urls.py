from django.urls import path,include
from . import views

urlpatterns = [
    path('signup',views.register,name='signup'),
    path('signin',views.login,name='signin'),
    path('logout',views.logout,name='logout'),
    path('<int:course_id>/bkash',views.bkash_from,name='bkash'),
]