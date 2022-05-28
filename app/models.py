from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Otp(models.Model):
    Otp = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

class Profile(models.Model):
    pro_user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    pro_img = models.ImageField(null=True, blank=True)

class VideosUpload(models.Model):
    vid_user = models.ForeignKey(User, on_delete = models.CASCADE)
    firstName = models.CharField(max_length=100)
    lastname= models.CharField(max_length=100)
    pic = models.CharField(max_length=300)
    video_tumb = models.ImageField(null=True)
    video_title = models.CharField(max_length=150)
    video_tags = models.CharField(max_length=200)
    video_like = models.IntegerField(default=0)
    video = models.FileField(null=True)

    def __str__(self):
        return self.video_title