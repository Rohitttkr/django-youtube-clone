from django.contrib import admin
from .models import Otp, Profile, VideosUpload

# Register your models here.

admin.site.register(Otp)
admin.site.register(Profile)
admin.site.register(VideosUpload)