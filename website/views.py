from re import sub
from readline import redisplay
from django import http
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import *
# Create your views here.

def index(request):
    sub_form = NewsletterSubscriptionForm()
    form = ContactMessageForm()
    context = {'sub_form': sub_form, 'form':form}

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
    return render(request, 'resources.html')

def events(request):
    return render(request, 'events.html')

def projects (request):
    return render(request, 'projects.html')


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