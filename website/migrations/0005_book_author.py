# Generated by Django 4.1.1 on 2022-09-29 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_book_cover_alter_book_book_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=255, null=True),
        ),
    ]