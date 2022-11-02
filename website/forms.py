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
            'other_amount_to_give':TextInput(attrs={'class': 'form-control', 'placeholder': 'Si vous avez choisi autre, entrez le montant que vous souhaitez donner'}),
            'first_name':TextInput(attrs={'class': 'form-control', 'placeholder': 'Ton prénom'}),
            'last_name':TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre nom de famille'}),
            'phone_number':TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre numéro de téléphone'}),            
            'country':TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre pays'}),            
            'email':EmailInput(attrs={'class': 'form-control', 'placeholder': 'Votre adresse e-mail'}),           
            'message':Textarea(attrs={'class': 'form-control', 'placeholder': 'Votre message'}),           
        }


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['first_name', 'last_name', 
        'phone_number', 'email', 'date', 'notes']

        widgets = {
            'first_name':TextInput(attrs={'class': 'form-control', 'placeholder': 'Ton prénom'}),
            'last_name':TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre nom de famille'}),
            'phone_number':TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre numéro de téléphone'}),            
            'date':DatePickerInput(attrs={'class': 'form-control', 'placeholder': 'Votre pays'}),            
            'email':EmailInput(attrs={'class': 'form-control', 'placeholder': 'Votre adresse e-mail'}),           
            'notes':Textarea(attrs={'class': 'form-control', 'placeholder': 'Des notes qui nous aideraient dans notre session?'}),           
        }


class NewsletterSubscriptionForm(ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ['name', 'email']
        widgets = {
            'name':TextInput(attrs={'class': 'form-control', 'placeholder': 'Ton nom complet'}),
            'email':EmailInput(attrs={'class': 'form-control', 'placeholder': 'Votre adresse e-mail'}),
        }

class GetInvolvedLeadForm(ModelForm):
    class Meta:
        model = GetInvolvedLead
        fields = ['name', 'email']
        widgets = {
            'name':TextInput(attrs={'class': 'form-control', 'placeholder': 'Ton nom complet'}),
            'email':EmailInput(attrs={'class': 'form-control', 'placeholder': 'Votre adresse e-mail'}),
        }



class ContactMessageForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['full_name', 'phone_number', 'email', 'message']
        widgets = {
            'full_name':TextInput(attrs={'class': 'form-control', 'placeholder': 'Ton nom complet'}),
            'phone_number':TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre numéro de téléphone'}),            
            'email':EmailInput(attrs={'class': 'form-control', 'placeholder': 'Votre adresse e-mail'}),           
            'message':Textarea(attrs={'class': 'form-control', 'placeholder': 'Votre message'}),           
        }