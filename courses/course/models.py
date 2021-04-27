from django.db import models

# Create your models here.

class All_course(models.Model):
    course_num = models.IntegerField(default=0)
    title = models.CharField(max_length=5000)
    price = models.IntegerField(default=1000)
    image = models.ImageField(upload_to='images/')
    intro_text = models.CharField(default="",max_length=5000)

    def __str__(self):
        return 'Course_num: {}; title: {};'.format(self.course_num, self.title)
    
    
class All_lesson(models.Model):
    lesson_num = models.IntegerField(default=0)
    course_num =  models.IntegerField(default=0)
    title = models.CharField(max_length=5000)
    link = models.URLField(max_length=500)

    def __str__(self):
        return 'course_num: {}; lesson_num: {};'.format(self.course_num, self.lesson_num)


class Review(models.Model):
    username = models.CharField(max_length=50)
    course_id = models.IntegerField()
    summary = models.CharField(max_length=250)
    ratting = models.IntegerField(default=5)
    permission = models.IntegerField(default=0)
    def __str__(self):
        return 'Course_num: {}; username: {};'.format(self.course_id, self.username)

class ki_ki_sikhben(models.Model):
    course_num =  models.IntegerField(default=0)
    details=models.CharField((""),max_length=2000);
    def __str__(self):
        return 'Course_num: {}; Details: {};'.format(self.course_num, self.details)

class course_details(models.Model):
    course_num =  models.IntegerField(default=0)
    keno_korben = models.CharField((""), max_length=1000)
    keno_korben_details = models.CharField((""), max_length=10000)
    ki_ki_sikhte_parben = models.CharField((""), max_length=1000)
    ki_ki_sikhte_parben_details = models.ManyToManyField(ki_ki_sikhben,verbose_name="list of sites")

    def __str__(self):
        return 'Course_num: {}; keno_korben: {};'.format(self.course_num, self.keno_korben)



class contact_form(models.Model):
    name=models.CharField("",max_length=100)
    email=models.CharField("",max_length=100)
    message=models.CharField("",max_length=1000)

    def __str__(self):
        return 'name: {}; email: {};'.format(self.name, self.email)