from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    #path('contact-form/', views.contactForm, name='contact-form'),
    path('nous-connaitre/', views.about, name='nous-connaitre'),
    path('conseils/', views.conseils, name='conseils'),
    path('resources/', views.resources, name='resources'),
    path('events/', views.events, name='events'),
    path('projets/', views.projets, name='projets'),
    path('faire-un-don/', views.faireUnDon, name='faire-un-don'),
    path('search/', views.search, name='search')
]