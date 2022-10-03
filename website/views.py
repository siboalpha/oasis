import imp
from django import http
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import *
# Create your views here.

def index(request):
    sub_form = NewsletterSubscriptionForm()
    form = ContactMessageForm()

    projects = Project.objects.order_by("-date_created")[:4]
    events = Event.objects.order_by("-date_created")[:4]

    context = {'sub_form': sub_form, 'form':form, 'projects':projects, 'events':events}

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
    context = {'form':form}
    if request.method == 'POST': 
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'contact.html', context)

def about(request):
    form = GetInvolvedLeadForm()
    context = {'form':form}
    if request.method =='POST':
        form = GetInvolvedLeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'about-us.html', context)

def counselling(request):
    form = AppointmentForm()
    context = {'form': form}
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'counseling.html', context)

def resources(request):
    podcasts = Podcast.objects.order_by("-date_created")[:4]
    context = {'podcasts':podcasts}
    return render(request, 'resources.html', context)

def events(request):
    events = Event.objects.all()
    context = {'events':events}
    return render(request, 'events.html', context)

def projects (request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'projects.html', context)


def donate(request):
    form = DonationForm()
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return HttpResponse('Data is not valid')
    
    context = {'form':form}
    return render(request, 'donate.html', context)

def search(request):
    from django.db.models import Q

    query = request.GET.get('q','')
    if query:
        queryset = (Q(title__icontains=query) | Q(details__icontains=query))
        podcasts = Podcast.objects.filter(queryset).distinct()
        music = RelaxingMusic.objects.filter(queryset).distinct()
        events = Event.objects.filter(queryset).distinct()
        projects = Project.objects.filter(queryset).distinct()
        context = {'podcasts':podcasts, 'music':music, 'events':events, 'projects':projects, 'query':query}
        return render (request, 'search.html', context)
    else:
        return render (request, 'search.html')