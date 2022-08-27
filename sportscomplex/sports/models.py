from django.db import models
from tkinter import CASCADE
from users.models import Member

# Create your models here.

class Sport(models.Model):
    name = models.CharField(max_length=20, unique = True )
    img_url = models.CharField(max_length=2083, default = 'https://alumni.iitd.ac.in/home/wp-content/uploads/2022/03/msc-930x620.png')

class Equipment(models.Model):
    name = models.CharField(max_length=20, unique = True )
    quantity = models.IntegerField(max_length=5, unique = True )
    sport = models.ForeignKey(Sport,on_delete=models.CASCADE)

class Court(models.Model):
    name = models.CharField(max_length=20, unique = True )
    sport = models.ForeignKey(Sport,on_delete=models.CASCADE)

class Slot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    court = models.ForeignKey(Court,on_delete=models.CASCADE)
    is_booked = models.BooleanField(default = False)
    booked_by = models.ForeignKey(Member, null = True, blank = True,on_delete=models.DO_NOTHING)