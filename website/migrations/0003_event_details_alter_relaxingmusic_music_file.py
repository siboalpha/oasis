# Generated by Django 4.1.1 on 2022-09-29 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_podcast_featured_image_alter_event_featured_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='details',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='relaxingmusic',
            name='music_file',
            field=models.FileField(upload_to='relaxing_music/music_files'),
        ),
    ]
