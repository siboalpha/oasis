# Generated by Django 4.1.1 on 2022-09-29 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_event_details_alter_relaxingmusic_music_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(null=True, upload_to='books/covers'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_file',
            field=models.FileField(upload_to='books/book_file'),
        ),
    ]