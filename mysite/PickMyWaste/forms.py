from django import forms
from .models import Food, Donators
from django.shortcuts import render, get_object_or_404


  

class DateInput(forms.DateInput):
    input_type = 'date'

class CreateNewListing(forms.Form):
    donator=forms.ModelChoiceField(label="Select User", queryset=Donators.objects.all())
    title = forms.CharField(label="Food Name", max_length=100)
    description = forms.CharField(label="description", max_length=10000)
    expiration_date = forms.DateField(label = 'expiration date', widget = DateInput)
    prepackaged = forms.NullBooleanField(label= 'prepackaged')
    perishable = forms.NullBooleanField(label='perishable')



    
class FilterFoodList(forms.Form):
    donator=forms.ModelChoiceField(label="Select User", queryset=Donators.objects.all())

    




