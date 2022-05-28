from dataclasses import field
from pyexpat import model
from django import forms
from .models import VideosUpload

class VideoFrom(forms.ModelForm):
    class Meta:
        model = VideosUpload
        fields = ("video_tumb", "video_title", "video_tags", "video")