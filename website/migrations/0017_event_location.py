# Generated by Django 4.1.1 on 2022-10-03 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_project_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
