# Generated by Django 4.0.3 on 2022-05-28 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_videosupload_delete_videos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videosupload',
            name='video_like',
            field=models.IntegerField(default=0),
        ),
    ]
