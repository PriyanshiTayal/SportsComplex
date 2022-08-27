from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Admin(models.Model):
    user = models.OneToOneField(User, primary_key = True,on_delete=models.CASCADE)

class Staff(models.Model):
    user = models.OneToOneField(User, primary_key = True,on_delete=models.CASCADE)

class Member(models.Model):
    user = models.OneToOneField(User, primary_key = True,on_delete=models.CASCADE)