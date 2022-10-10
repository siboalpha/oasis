# Generated by Django 4.1.1 on 2022-10-07 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0024_delete_library'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('Bonheur Familiale', 'Bonheur Familiale'), ('Vie spirituelle', 'Vie spirituelle'), ('Jeunesse', 'Jeunesse'), ('Vie quotidienne', 'Vie quotidienne')], default='Jeunesse', max_length=255),
        ),
    ]