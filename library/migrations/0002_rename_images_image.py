# Generated by Django 4.1.1 on 2022-10-06 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='images',
            new_name='Image',
        ),
    ]
