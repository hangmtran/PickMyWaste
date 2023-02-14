from django.urls import path

from . import views
from PickMyWaste import views as view


urlpatterns = [
    path("",views.index, name='index'),
    path('home/', views.home, name = "home"),
    path('create/', views.create, name='create'),
    path('<int:id>/',views.view_food, name="view_food"),
    path('foodlist/', views.list_food, name="food_list"),
    path('register/', views.register, name="register"),
    path('map/',view.map, name="map")


]


