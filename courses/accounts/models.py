from django.db import models
from django.utils.timezone import now



class bkash(models.Model):
    username = models.CharField(max_length=250,default="")
    email = models.CharField(max_length=250)
    mobile_number = models.CharField(max_length=15,default="")
    transaction_id = models.CharField(max_length=40)
    course_id = models.IntegerField(default=1)
    permision = models.IntegerField(default=5)
    
class contact(models.Model):
    username = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    mobile_number = models.CharField(max_length=15,default="")
