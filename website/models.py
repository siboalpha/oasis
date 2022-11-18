from django.utils import timezone
from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse

# Create your models here.

class Appointment(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    date_created = models.DateTimeField(default=timezone.now)
    date = models.DateField(auto_now_add=False)
    notes = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name

class Podcast(models.Model):
    date_created = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True)
    details = models.TextField(max_length=500, null=True)
    author = models.CharField(max_length=255)
    podcat_file = models.FileField(upload_to = 'podcasts')
    featured_image = models.ImageField(upload_to = 'podcasts/featured_images', null = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('podcast', kwargs={'slug': self.slug})

class RelaxingMusic(models.Model):
    date_created = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True)
    details = models.TextField(max_length=500, null=True)
    author = models.CharField(max_length=255)
    featured_image = models.ImageField(upload_to = 'relaxing_music/featured_images')
    music_file = models.FileField(upload_to = 'relaxing_music/music_files')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('relaxing-music', kwargs={'slug': self.slug})

class Event(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True)
    featured_image = models.ImageField(upload_to = 'events/featured_images')
    details = models.TextField(max_length=500, null = True)
    date = models.DateField(auto_now_add=False)
    location = models.CharField(max_length=255, null=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event', kwargs={'slug': self.slug})


class Project(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True)
    details = models.TextField(max_length=255)
    featured_image = models.ImageField(upload_to = 'projects/featured_images')
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('projet', kwargs={'slug': self.slug})


class Book(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True)
    author = models.CharField(max_length = 255, null = True)
    cover = models.ImageField(upload_to = 'books/covers', null = True)
    details = models.TextField(max_length=500)
    book_file = models.FileField(upload_to = 'books/book_file')
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book', kwargs={'slug': self.slug})

class ContactMessage(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    date_created = models.DateTimeField(default=timezone.now, null = True)
    message = models.TextField(max_length = 500, null = True)

    def __str__(self):
        return self.full_name


class Donation(models.Model):
    Mobiel_Money = 'Argent mobile'
    Bank_transfer = 'Transfert bancaire'
    Cheque = 'Chèque'
    Cash = 'En espèces'


    ten = '$10'
    twenty = '$20'
    fifty = '$50'
    hundred = '$100'
    two_hundred = '$200'
    other = 'Autre'

    AMOUNT_TO_GIVE_CHOICES = [
        (ten , '$10'),
        (twenty , '$20'),
        (fifty , '$50'),
        (hundred , '$100'),
        (two_hundred , '$200'),
        (other, 'Autre')
    ]

    WAYS_TO_GIVE_CHOICES = [
        (Mobiel_Money, 'Argent mobile'),
        (Bank_transfer, 'Transfert bancaire'),
        (Cheque, 'Chèque'),
        (Cash, 'En espèces'),
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

    def __str__(self):
        return self.first_name


class NewsletterSubscription(models.Model):
    name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)

    def __str__(self):
        return self.name


class GetInvolvedLead(models.Model):
    name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)

    def __str__(self):
        return self.name

class Blog(models.Model):
    Vie_spirituelle = 'Vie spirituelle'
    Vie_quotidienne = 'Vie quotidienne'
    Bonheur_Familiale = 'Bonheur Familiale'
    Jeunesse  = 'Jeunesse'

    BLOG_CATEGORIES = {
        (Vie_spirituelle , 'Vie spirituelle'),
        (Vie_quotidienne, 'Vie quotidienne'),
        (Bonheur_Familiale, 'Bonheur Familiale'),
        (Jeunesse, 'Jeunesse')

    }

    title = models.CharField(max_length = 255)
    slug = models.SlugField(unique = True, null = True)
    category = models.CharField(max_length = 255, choices = BLOG_CATEGORIES, default = Jeunesse)
    date_created = models.DateTimeField(default=timezone.now, null = True)
    autho = models.CharField(max_length = 255, null=True)
    featured_image = models.ImageField(upload_to = "blog/fratured_image")
    summary = models.TextField(max_length = 255, null = True)
    content = RichTextField(max_length = 5000)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog', kwargs={"slug": self.slug})
