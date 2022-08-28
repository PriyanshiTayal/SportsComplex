from django.db import models
from tkinter import CASCADE
from users.models import Member

# Create your models here.

class Sport(models.Model):
    name = models.CharField(max_length=20, unique = True )
    img_url = models.CharField(max_length=2083, default = 'https://uploads-ssl.webflow.com/617b224ba2374548fcc039ba/617b224ba237453ce1c0409b_hpfulq-1234-1024x512.jpg')
    
class Equipment(models.Model):
    name = models.CharField(max_length=20, unique = True )
    quantity = models.IntegerField( unique = True )
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