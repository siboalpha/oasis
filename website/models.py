from distutils.command.upload import upload
from email import message
from email.policy import default
from random import choices
from turtle import title
from unicodedata import name
from django.forms import ChoiceField
from django.utils import timezone
from django.db import models

# Create your models here.

class Appointment(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    date_created = models.DateTimeField(default=timezone.now)
    date = models.DateField(auto_now_add=False)
    notes = models.CharField(max_length=255)

class Podcast(models.Model):
    date_created = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    podcat_file = models.FileField(upload_to = 'podcasts')
    featured_image = models.ImageField(upload_to = 'podcasts/featured_images', null = True)

class RelaxingMusic(models.Model):
    date_created = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    featured_image = models.ImageField(upload_to = 'relaxing_music/featured_images')
    music_file = models.FileField(upload_to = 'relaxing_music/music_files')

class Event(models.Model):
    title = models.CharField(max_length=255)
    featured_image = models.ImageField(upload_to = 'events/featured_images')
    details = models.TextField(max_length=500, null = True)
    date = models.DateField(auto_now_add=False)
    date_created = models.DateTimeField(default=timezone.now)

class Project(models.Model):
    title = models.CharField(max_length=255)
    desciprion = models.TextField(max_length=255)
    featured_image = models.ImageField(upload_to = 'projects/featured_images')

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length = 255, null = True)
    cover = models.ImageField(upload_to = 'books/covers', null = True)
    summary = models.TextField(max_length=500)
    book_file = models.FileField(upload_to = 'books/book_file')
    date_created = models.DateTimeField(default=timezone.now)


class ContactMessage(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    date_created = models.DateTimeField(default=timezone.now, null = True)
    message = models.TextField(max_length = 500, null = True)


class Donation(models.Model):
    Mobiel_Money = 'Mobile money'
    Bank_transfer = 'Bank transfer'
    Cheque = 'Cheque'
    Cash = 'Cash'


    ten = '$10'
    twenty = '$20'
    fifty = '$50'
    hundred = '$100'
    two_hundred = '$200'
    other = 'other'

    AMOUNT_TO_GIVE_CHOICES = [
        (ten , '$10'),
        (twenty , '$20'),
        (fifty , '$50'),
        (hundred , '$100'),
        (two_hundred , '$200'),
        (other, 'other')
    ]

    WAYS_TO_GIVE_CHOICES = [
        (Mobiel_Money, 'Mobile money'),
        (Bank_transfer, 'Bank Transfer'),
        (Cheque, 'Cheque'),
        (Cash, 'Cash'),
    ]
    ways_to_give = models.CharField(max_length = 255, choices=WAYS_TO_GIVE_CHOICES, default=Mobiel_Money)
    amount_to_give = models.CharField(max_length = 255, choices=AMOUNT_TO_GIVE_CHOICES, default=two_hundred)
    other_amount_to_give = models.CharField(max_length = 255, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    date_created = models.DateTimeField(default=timezone.now)
    message = models.CharField(max_length=255)


class NewsletterSubscription(models.Model):
    name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)

class GetInvolvedLead(models.Model):
    name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)