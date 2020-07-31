from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=350)
    text = models.TextField(max_length=10000)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)



