from django.urls import path

from . import views

from .models import Donators

urlpatterns = [
    path('', views.index, name='index'),
    path('foodMap/', views.foodMap, name='foodMap'),
    # path('create/', views.create, name='create'),



]

#views as class
