from django.contrib import admin
from .models import All_course,All_lesson,Review,ki_ki_sikhben,course_details,contact_form

# Register your models here.
admin.site.register(All_course)
admin.site.register(All_lesson)
admin.site.register(Review)
admin.site.register(ki_ki_sikhben)
admin.site.register(course_details)
admin.site.register(contact_form)
