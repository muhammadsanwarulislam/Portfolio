from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Article(models.Model):
    title     = models.CharField(max_length = 30)
    content   = models.TextField()
    created_by= models.ForeignKey(User,on_delete=models.CASCADE)
    created_on= models.DateField(default = timezone.now)

    def __str__(self):
        return self.title