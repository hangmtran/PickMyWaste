
# Create your models here.
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from localflavor.us.models import USStateField
from address.models import AddressField




class Donators(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    email=models.EmailField(max_length=254, default='')
    address = AddressField(on_delete=models.CASCADE, default="")
    zipcode = models.CharField(max_length=200,blank=True, null=True)
    state = USStateField(null=True, blank=True)
    country = models.CharField(max_length=200,blank=True, null=True)
    latitude = models.CharField(max_length=200,blank=True, null=True)
    longitude = models.CharField(max_length=200,blank=True, null=True)

    def __str__(self):
        return self.name


class Food(models.Model):
    donator = models.ForeignKey(Donators, on_delete=models.CASCADE,blank=True, null=True, default=None)
    title = models.CharField(max_length=100, blank = False)
    description = models.CharField(max_length=10000)
    expiration_date= models.DateField(null= True)
    pub_date = models.DateField(auto_now_add = True)
    prepackaged = models.BooleanField(null=True, blank=True)
    perishable = models.BooleanField(null=True, blank=True)
    
    def __str__(self):
        return self.title


    
