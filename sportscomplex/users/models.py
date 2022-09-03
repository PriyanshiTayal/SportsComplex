from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class Admin(models.Model):
    user = models.OneToOneField(User, primary_key = True,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user.username}'

class Staff(models.Model):
    user = models.OneToOneField(User, primary_key = True,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user.username}'

class Member(models.Model):
    user = models.OneToOneField(User, primary_key = True,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user.username}'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
            Member.objects.create(user=instance)
