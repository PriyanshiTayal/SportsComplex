from django.db import models
from tkinter import CASCADE
from users.models import Member
from datetime import date
from django.contrib.auth.models import User
# Create your models here.

class Sport(models.Model):
    name = models.CharField(max_length=20, unique = True , help_text = '(Please, use underscore(_) or hypen(-) in place of spaces.)')
    img_url = models.CharField(max_length=2083, verbose_name = 'Image', help_text = '(Copy-paste the sport-image url here)', default = 'https://uploads-ssl.webflow.com/617b224ba2374548fcc039ba/617b224ba237453ce1c0409b_hpfulq-1234-1024x512.jpg')
    def __str__(self):
        return f'{self.name}'

class Equipment(models.Model):
    name = models.CharField(max_length=20)
    quantity = models.IntegerField( )
    sport = models.ForeignKey(Sport,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name}'

class Court(models.Model):
    name = models.CharField(max_length=20, unique = True )
    sport = models.ForeignKey(Sport,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name}'

class Slot(models.Model):
    start_time = models.TimeField(help_text = "(Time should be of format HH:MM from 00:00 to 23:59.)")
    end_time = models.TimeField(help_text = "(Time should be of format HH:MM from 00:00 to 23:59.)")
    date = models.DateField(default = date.today(),help_text = "(Date should be of format YYYY-MM-DD)")
    court = models.ForeignKey(Court,on_delete=models.CASCADE)
    message = models.CharField(max_length=200, null = True, blank = True)
    def __str__(self):
        return f'{self.court.name}'    

class Booking(models.Model):
    time_slot = models.OneToOneField(Slot, on_delete=models.CASCADE)
    booked_by = models.ForeignKey(User, null = True, blank = True,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.booked_by}'