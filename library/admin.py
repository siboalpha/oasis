from django.contrib import admin
from django.template import Library
from . models import *
# Register your models here.

@admin.register(Image)
class BlogAdmin(admin.ModelAdmin):
     list_display = ("title", "image")

@admin.register(Video)
class BlogAdmin(admin.ModelAdmin):
     list_display = ("title", "video")
