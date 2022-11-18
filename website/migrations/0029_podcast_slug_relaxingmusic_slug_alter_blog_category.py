# Generated by Django 4.1.1 on 2022-11-09 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0028_book_slug_event_slug_project_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='relaxingmusic',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('Vie spirituelle', 'Vie spirituelle'), ('Vie quotidienne', 'Vie quotidienne'), ('Bonheur Familiale', 'Bonheur Familiale'), ('Jeunesse', 'Jeunesse')], default='Jeunesse', max_length=255),
        ),
    ]