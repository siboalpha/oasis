# Generated by Django 4.1.1 on 2022-10-06 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_event_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='ways_to_give',
            field=models.CharField(choices=[('Argent mobile', 'Argent mobile'), ('Transfert bancaire', 'Bank Transfer'), ('Chèque', 'Transfert bancaire'), ('En espèces', 'En espèces')], default='Argent mobile', max_length=255),
        ),
    ]
