from django import forms
from .models import Donators
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
    address=forms.CharField(label="Address", max_length=100)
    phone=PhoneNumberField(label="Phone")
    email=forms.EmailField(label="Email Address")
  




    


