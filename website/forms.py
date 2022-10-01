from dataclasses import field, fields
from statistics import mode
from django import forms
from django.forms import ModelForm, TextInput, Textarea, RadioSelect, EmailInput
from .models import *


class DatePickerInput(forms.DateInput):
        input_type = 'date'
class TimePickerInput(forms.TimeInput):
        input_type = 'time'

class DonationForm(ModelForm):
    class Meta:
        model = Donation
        fields = ['ways_to_give', 'amount_to_give', 
        'other_amount_to_give', 'first_name', 'last_name', 
        'phone_number', 'country', 'email', 'message' ]

        widgets = {
            'ways_to_give':RadioSelect(attrs={'class':'multiple-inputs'}),
            'amount_to_give':RadioSelect(attrs={'class': 'multiple-inputs'}),
            'other_amount_to_give':TextInput(attrs={'class': 'form-control', 'placeholder': 'If you chose other, enter what you want to give'}),
            'first_name':TextInput(attrs={'class': 'form-control', 'placeholder': 'Your first name'}),
            'last_name':TextInput(attrs={'class': 'form-control', 'placeholder': 'Your last name'}),
            'phone_number':TextInput(attrs={'class': 'form-control', 'placeholder': 'Your phone number'}),            
            'country':TextInput(attrs={'class': 'form-control', 'placeholder': 'Your country'}),            
            'email':EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email Address'}),           
            'message':Textarea(attrs={'class': 'form-control', 'placeholder': 'Your message'}),           
        }


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['first_name', 'last_name', 
        'phone_number', 'email', 'date', 'notes']

        widgets = {
            'first_name':TextInput(attrs={'class': 'form-control', 'placeholder': 'Your first name'}),
            'last_name':TextInput(attrs={'class': 'form-control', 'placeholder': 'Your last name'}),
            'phone_number':TextInput(attrs={'class': 'form-control', 'placeholder': 'Your phone number'}),            
            'date':DatePickerInput(attrs={'class': 'form-control', 'placeholder': 'Your country'}),            
            'email':EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email Address'}),           
            'notes':Textarea(attrs={'class': 'form-control', 'placeholder': 'Any notes that would help us in our session?'}),           
        }


class NewsletterSubscriptionForm(ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ['name', 'email']
        widgets = {
            'name':TextInput(attrs={'class': 'form-control', 'placeholder': 'Your full name'}),
            'email':EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email address'}),
        }

class GetInvolvedLeadForm(ModelForm):
    class Meta:
        model = GetInvolvedLead
        fields = ['name', 'email']
        widgets = {
            'name':TextInput(attrs={'class': 'form-control', 'placeholder': 'Your full name'}),
            'email':EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email address'}),
        }



class ContactMessageForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['full_name', 'phone_number', 'email', 'message']
        widgets = {
            'full_name':TextInput(attrs={'class': 'form-control', 'placeholder': 'Your full name'}),
            'phone_number':TextInput(attrs={'class': 'form-control', 'placeholder': 'Your phone number'}),            
            'email':EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email Address'}),           
            'message':Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message'}),           
        }