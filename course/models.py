from django.db import models

# Create your models here.

class All_course(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=250)
    price = models.IntegerField(default=1000)
    image = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.title
    
    
class All_lesson(models.Model):
    lesson_Num = models.IntegerField()
    course_Num =  models.IntegerField()
    title = models.CharField(max_length=250)
    link = models.URLField()

    def __str__(self):
        return self.title


class Review(models.Model):
    username = models.CharField(max_length=50)
    course_id = models.IntegerField()
    summary = models.CharField(max_length=250)
    rating = models.IntegerField()

    def __str__(self):
        return self.username

