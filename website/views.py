import imp
from django import http
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import *
from library.models import Image
# Create your views here.

def index(request):
    sub_form = NewsletterSubscriptionForm()
    form = ContactMessageForm()

    projects = Project.objects.order_by("-date_created")[:4]
    events = Event.objects.order_by("-date_created")[:4]

    footer_events = Event.objects.order_by("date_created")[:4]
    footer_books = Book.objects.order_by("-date_created")[:2]
    context = {'sub_form': sub_form, 'form':form, 'projects':projects, 'events':events, 'footer_events':footer_events, 'footer_books':footer_books}

    if request.method == 'POST':
        sub_form = NewsletterSubscriptionForm(request.POST)
        form = ContactMessageForm(request.POST)
        if sub_form.is_valid():
            sub_form.save()
            return redirect('contact')
        if form.is_valid():
            form.save()
            return redirect('contact')
    return render(request, 'index.html', context)

def contact(request):
    form = ContactMessageForm()

    footer_events = Event.objects.order_by("date_created")[:4]
    
    context = {'form':form, 'footer_events':footer_events}
    if request.method == 'POST': 
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'contact.html', context)

def about(request):
    form = GetInvolvedLeadForm()
    footer_events = Event.objects.order_by("date_created")[:4]
    context = {'form':form, 'footer_events':footer_events}
    if request.method =='POST':
        form = GetInvolvedLeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'nous-connaitre.html', context)

def conseils(request):
    form = AppointmentForm()
    footer_events = Event.objects.order_by("date_created")[:4]

    context = {'form': form, 'footer_events':footer_events}
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'conseils.html', context)

def resources(request):
    podcasts = Podcast.objects.order_by("-date_created")[:4]
    footer_events = Event.objects.order_by("date_created")[:4]

    music = RelaxingMusic.objects.order_by("-date_created")[:4]
    blogsJeunesse = Blog.objects.order_by("-date_created").filter(category = 'Jeunesse')[:4]
    blogsBonheur_Familiale = Blog.objects.order_by("-date_created").filter(category = 'Bonheur Familiale')[:4]
    print(blogsBonheur_Familiale.count)
    blogsVie_quotidienne = Blog.objects.order_by("-date_created").filter(category = 'Vie quotidienne')[:4]
    blogsVie_spirituelle = Blog.objects.order_by("-date_created").filter(category = 'Vie spirituelle')[:4]
    context = {'podcasts':podcasts, 'music':music, 'blogsJeunesse':blogsJeunesse, 'blogsBonheur_Familiale':blogsBonheur_Familiale,
    'blogsVie_quotidienne':blogsVie_quotidienne, 'blogsVie_spirituelle':blogsVie_spirituelle, 'footer_events':footer_events}
    return render(request, 'resources.html', context)

def events(request):
    events = Event.objects.all()
    footer_events = Event.objects.order_by("date_created")[:4]
    context = {'events':events, 'footer_events':footer_events}
    return render(request, 'events.html', context)

def projets (request):
    projects = Project.objects.all()
    footer_events = Event.objects.order_by("date_created")[:4]

    context = {'projects':projects, 'footer_events':footer_events}
    return render(request, 'projets.html', context)


def faireUnDon(request):
    form = DonationForm()
    footer_events = Event.objects.order_by("date_created")[:4]
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return HttpResponse('Data is not valid')
    
    context = {'form':form, 'footer_events':footer_events}
    return render(request, 'faire-un-don.html', context)

def search(request):
    from django.db.models import Q
    footer_events = Event.objects.order_by("date_created")[:4]
    query = request.GET.get('q','')
    if query:
        queryset = (Q(title__icontains=query) | Q(details__icontains=query))
        podcasts = Podcast.objects.filter(queryset).distinct()
        music = RelaxingMusic.objects.filter(queryset).distinct()
        events = Event.objects.filter(queryset).distinct()
        projects = Project.objects.filter(queryset).distinct()
        context = {'podcasts':podcasts, 'music':music, 'events':events, 'projects':projects, 'query':query ,'footer_events':footer_events}
        return render (request, 'search.html', context)
    else:
        return render (request, 'search.html')


def blog(request, slug):
    blog = Blog.objects.get(slug = slug)
    context = {'blog':blog}
    return render(request, 'blog.html', context)


def projet(request, slug):
    blog = Project.objects.get(slug = slug)
    context = {'blog':blog}
    return render(request, 'projet.html', context)

def event(request, slug):
    event = Event.objects.get(slug = slug)
    context = {'event':event}
    return render(request, 'event.html', context)

def podcast(request, slug):
    podcast = Podcast.objects.get(slug = slug)
    context = {'podcast':podcast}
    return render(request, 'podcast.html', context)