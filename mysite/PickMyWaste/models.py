

# Create your models here.
import datetime
from django.db import models
from django.utils import timezone




    



class Donators(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    address = models.CharField(max_length=300, default='')
    phone = models.CharField(max_length=100,default='')
   
    
    

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

     # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    
