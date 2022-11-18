# Generated by Django 4.1.1 on 2022-11-09 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0026_blog_summary_alter_blog_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('Vie quotidienne', 'Vie quotidienne'), ('Bonheur Familiale', 'Bonheur Familiale'), ('Jeunesse', 'Jeunesse'), ('Vie spirituelle', 'Vie spirituelle')], default='Jeunesse', max_length=255),
        ),
    ]
