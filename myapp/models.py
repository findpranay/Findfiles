from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length=100)
    image= models.ImageField(upload_to='images')
    author = models.ForeignKey(User,default=None,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=100)
    video= models.FileField(upload_to='video')
    author = models.ForeignKey(User,default=None,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Pdf(models.Model):
    title = models.CharField(max_length=100)
    pdf= models.FileField(upload_to='pdf')
    author = models.ForeignKey(User,default=None,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
