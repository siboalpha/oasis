# Generated by Django 4.1.1 on 2022-09-29 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='featured_image',
            field=models.ImageField(null=True, upload_to='podcasts/featured_images'),
        ),
        migrations.AlterField(
            model_name='event',
            name='featured_image',
            field=models.ImageField(upload_to='events/featured_images'),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='podcat_file',
            field=models.FileField(upload_to='podcasts'),
        ),
        migrations.AlterField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(upload_to='projects/featured_images'),
        ),
        migrations.AlterField(
            model_name='relaxingmusic',
            name='featured_image',
            field=models.ImageField(upload_to='relaxing_music/featured_images'),
        ),
        migrations.AlterField(
            model_name='relaxingmusic',
            name='music_file',
            field=models.FileField(upload_to='music/relaxing_music/music_files'),
        ),
    ]
