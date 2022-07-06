from django.db import models 
from django.contrib.auth.models import User


class Center(models.Model):
    name = models.CharField(max_length=255)
    noOfBookings = models.PositiveSmallIntegerField(default=0)


class MyUser(models.Model):
    age = models.PositiveSmallIntegerField()
    center = models.ForeignKey(Center, on_delete=models.CASCADE)
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    


