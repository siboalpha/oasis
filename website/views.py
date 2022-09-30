from readline import redisplay
from django import http
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import *
# Create your views here.

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
     return render(request, 'about-us.html')

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