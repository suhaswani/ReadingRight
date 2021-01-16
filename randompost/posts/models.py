from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    body = models.TextField(max_length=1000)


