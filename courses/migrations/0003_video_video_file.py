# Generated by Django 3.0.6 on 2020-08-01 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20200801_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='video_file',
            field=models.FileField(default='default.jpg', upload_to='courses_videos', verbose_name='course_video'),
        ),
    ]
