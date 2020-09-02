from django.db import models
from django.contrib.auth.models import User




# Create your models here.
class CourseDetails(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    category=models.CharField(max_length=200, null=True,blank=True)
    duration = models.CharField(max_length=20, null=True, blank=True)
    overview = models.CharField(max_length=2000, null=True, blank=True)
    lectures = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    img = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.title


class LecturesModel(models.Model):
    course=models.ForeignKey(CourseDetails,on_delete=models.CASCADE,null=True,blank=True)
    lect=models.CharField(max_length=500, null=True, blank=True)
    lect_number=models.CharField(max_length=500, null=True, blank=True)
    time=models.CharField(max_length=500,null=True, blank=True)
    type=models.CharField(max_length=500, null=True, blank=True)
    description=models.CharField(max_length=500, null=True, blank=True)



    def __str__(self):
        return self.lect

class Instructor(models.Model):
    title=models.ForeignKey(CourseDetails,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=50,null=True,blank=True)
    photo = models.FileField(null=True, blank=True)
    about = models.CharField(max_length=5000, null=True, blank=True)

    def __str__(self):
        return self.name

class UserDetails(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    number = models.CharField(max_length=10,null=True, blank=True)

    def __str__(self):
        return self.name

class Course_users(models.Model):
    usr=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    courses=models.CharField(max_length=5000, null=True, blank=True)

    def __str__(self):
        return self.name


class Checkout(models.Model):
    usr = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    course = models.ForeignKey(CourseDetails, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, default="Pending")
    course_idd = models.IntegerField(null=True, blank=True)

class Payment_Id(models.Model):
    Usr = models.ForeignKey(User, on_delete=models.CASCADE)
    PayId = models.CharField(max_length=120, null=True, blank=True)




