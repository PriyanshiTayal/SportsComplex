from django.db import models
from tkinter import CASCADE

# Create your models here.
class Slot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

class Sport(models.Model):
    name = models.CharField(max_length=20, unique = True )
    image = models.ImageField(default ='default.jpg', upload_to='pics')

class Equipment(models.Model):
    name = models.CharField(max_length=20, unique = True )
    quantity = models.IntegerField(max_length=5, unique = True )
    sport = models.ForeignKey(Sport,on_delete=models.CASCADE)

class Equipment(models.Model):
    name = models.CharField(max_length=20, unique = True )
    sport = models.ForeignKey(Sport,on_delete=models.CASCADE)
