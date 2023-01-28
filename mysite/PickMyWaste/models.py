from django.db import models

# Create your models here.
import datetime
from django.db import models
from django.utils import timezone


class Food(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=10000)
    expiration_date= models.DateTimeField('date published')
    #created at or update at by default?
    pub_date = models.DateTimeField('date published')
    prepackaged = models.BooleanField(null=True, blank=True)
    perishable = models.BooleanField(null=True, blank=True)


    def __str__(self):
        return self.title

    



class Donators(models.Model):
    food_listing = models.CharField(max_length=200)
    food_quantity = models.IntegerField(default=1)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.food_listing

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
