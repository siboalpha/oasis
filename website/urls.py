from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    #path('contact-form/', views.contactForm, name='contact-form'),
    path('about/', views.about, name='about'),
    path('counselling/', views.counselling, name='counselling'),
    path('resources/', views.resources, name='resources'),
    path('events/', views.events, name='events'),
    path('projects/', views.projects, name='projects'),
    path('donate/', views.donate, name='donate'),
    path('search/', views.search, name='search')
]