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
    prepopulated_fields = {"slug": ("title",)}


@admin.register(RelaxingMusic)
class RelaxingMusicAdmin(admin.ModelAdmin):
    list_display = ("title", "author")
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "date")
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "featured_image")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date_created")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone_number", "email", "date_created")

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email","ways_to_give", "amount_to_give", "other_amount_to_give", "date_created")

@admin.register(NewsletterSubscription)
class NewletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ("name", "email")

@admin.register(GetInvolvedLead)
class GetInvolvedLeadAdmin(admin.ModelAdmin):
    list_display = ("name", "email")

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
     list_display = ("title", "date_created")
     prepopulated_fields = {"slug": ("title",)}
