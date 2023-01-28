from django.contrib import admin

from .models import Food, Donators
# Register your models here.
admin.site.register(Food)
admin.site.register(Donators)