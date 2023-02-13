from django import forms
from .models import Food, Donators
from django.shortcuts import render, get_object_or_404
from phonenumber_field.formfields import PhoneNumberField




  

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

class DonatorRegistration(forms.Form):
    name=forms.CharField(label="Company Name", max_length=100)
    address=forms.CharField(label="address", max_length=100)
    phone=PhoneNumberField(label="phone")
    email=forms.EmailField(label="email")


# donator.phone.as_e164
# rom phonenumber_field.phonenumber import PhoneNumber
# phone = PhoneNumber.from_string(phone_number=raw_phone, region='RU').as_e164


    # class Donators(models.Model):
    # name = models.CharField(max_length=100, blank=False, default='')
    # address = models.CharField(max_length=300, default='')
    # phone = models.CharField(max_length=100,default='')
    # email=models.EmailField(max_length=254)
   

    


