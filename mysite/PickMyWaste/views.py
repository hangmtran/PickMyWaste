from django.shortcuts import render
from .models import Food, Donators

from django.shortcuts import render, get_object_or_404

from .models import Food, Donators

# from .forms import CreateNewListing





def index(request):
    ls = Food.objects.get(id=id)
    latest_food_dict = {}
    latest_food_list = Food.objects.order_by('-pub_date')[:5]
    context = {'latest_food_list': latest_food_list}
    return render(request, 'pickmywaste/index.html', context)

def detail(request, donator_id):
   
    donator = get_object_or_404(Donators, pk=donator_id)
    return render(request, 'pickmywaste/.html', {'donator': donator})

def foodMap(response):
    return render(response,"pickmywaste/foodMap.html", {})

# #function for form food listing
# def create(response):
#     #check to see if post or get request(default is always get)
#     if response.method == "POST": 
#         form = CreateNewListing(response.POST)
#         if form.is_valid():
#             n = form.cleaned_data["title"] #form takes post and gets data from form. Clean data.type name of field we want)
#             t = Food(name=n)
#             t.save()  #creates a new list
#     else:
#         form = CreateNewListing()#create a blank form and pass to HTML
#     return render(response,"pickmywaste/create.html",{"form":form})
