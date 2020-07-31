from django.db import models
from django.utils import timezone


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=350)
    text = models.TextField()
    date = models.DateTimeField(editable=False)
    image = models.ImageField(upload_to='images', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.date = timezone.now()
        return super(Post, self).save(*args, **kwargs)
