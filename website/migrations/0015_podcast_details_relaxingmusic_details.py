# Generated by Django 4.1.1 on 2022-10-03 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_rename_summary_book_details_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='details',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='relaxingmusic',
            name='details',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
