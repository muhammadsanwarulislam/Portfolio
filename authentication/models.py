from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user        = models.OneToOneField(User,on_delete=models.CASCADE)
    pro_img     = models.ImageField(default = 'default.png',upload_to = 'profile_pic')
    designation = models.CharField(max_length = 50)
    location    = models.CharField(max_length = 50)

    def __str__(self):
        return f'{self.user.username} Profile'

class Contact(models.Model):
    email      = models.EmailField()
    subject    = models.CharField(max_length = 30)
    message    = models.TextField()
    created_on = models.DateField(default =timezone.now)

    def __str__(self):
        return self.email

@receiver(post_save,sender = User)
def created_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user = instance)

@receiver(post_save,sender = User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()