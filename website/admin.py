from django.contrib import admin
from django.urls import clear_script_prefix
from .models import *
# Register your models here.

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone_number", "date")


@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    list_display = ("title", "author")


@admin.register(RelaxingMusic)
class RelaxingMusicAdmin(admin.ModelAdmin):
    list_display = ("title", "author")


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "date")

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "featured_image")


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date_created")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone_number", "email", "date_created")

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email","ways_to_give", "amount_to_give", "other_amount_to_give", "date_created")