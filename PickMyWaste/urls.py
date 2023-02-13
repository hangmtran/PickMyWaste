from django.urls import path

from . import views

from .models import Food

urlpatterns = [
    path("",views.index, name='index'),
    # path('<int:id>', views.index, name='index'),
    path('home/', views.home, name = "home"),
    # path('foodMap/', views.foodMap, name='foodMap'),
    path('create/', views.create, name='create'),
    path('<int:id>/',views.view_food, name="view_food"),
    # path('delete_event/<event_id>', views.delete_event, name = 'delete-event'), 
    path('foodlist/', views.list_food, name="food_list"),
    path('register/', views.register, name="register"),
    
 


   
        
    



]

#views as class
