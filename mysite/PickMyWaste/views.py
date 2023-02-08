from django.shortcuts import render
from .models import Food, Donators

from django.shortcuts import render, get_object_or_404

from .models import Food, Donators

from .forms import CreateNewListing, FilterFoodList
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic.list import ListView




def index(request):
#     ls = Food.objects.get(id=id)
#     latest_food_dict = {}
    latest_food_list = Food.objects.order_by('-pub_date')[:5]
    context = {'latest_food_list': latest_food_list}
    return render(request, 'PickMyWaste/index.html', context)

# def index(response,id):
#     ls = Food.objects.get(id=id)
#     return render(response, "PickMyWaste/foodlist.html", {"ls":ls})


def home(response):
    return render(response, "PickMyWaste/home.html", {}) 


def detail(request, donator_id):
   
    donator = get_object_or_404(Donators, pk=donator_id)
    return render(request, 'pickmywaste/.html', {'donator': donator})

def foodMap(response):
    return render(response,"pickmywaste/foodMap.html")

#function for form food listing
def create(response): #change to create food, change to request
    #check to see if post or get request(default is always get)
    if response.method == "POST": 
        form = CreateNewListing(response.POST)
        if form.is_valid(): #is valid automatically exist b/c it inheritences from forms.Form and makes sure if valid input
            donator = form.cleaned_data["donator"]
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            expiration_date = form.cleaned_data["expiration_date"]
            # pub_date = form.cleaned_data["pub_date"]
            prepackaged = form.cleaned_data["prepackaged"]


            
             #form takes post and gets data from form. Clean data.type name of field we want)
            t = Food(donator=donator, title=title, description= description, expiration_date = expiration_date, prepackaged = prepackaged) #creating new food instance of food class, and set title from form
   
           
            t.save()  #creates a new list
         
        # redirect the page to the id of the foodlisting
            return redirect('view_food', id = t.id)

    else:
        form = CreateNewListing()#create a blank form and pass to HTML
    return render(response,"pickmywaste/create.html",{"form":form})

# def delete_event(request, event_id):
#     event = Food.objects()
# #     instance = Food.objects.get(id = id)
# #     instance.delete()

def view_food(request, id):
    food = Food.objects.get(id=id)
    return render (request,"PickMyWaste/food_view.html",{"food":food})




def list_food(response):
    if response.method == "POST": 
        form = FilterFoodList(response.POST)
        print(form)
        if form.is_valid():
            donator = form.cleaned_data["donator"]
            ls = Donators.objects.get(id = donator.id)
            food_list = Food.objects.filter(donator = ls)
            
            return render(response,"PickMyWaste/food_list.html",{"object_list":food_list, "form":form, "donor": ls})
    else:
         form = FilterFoodList()
    return render(response,"PickMyWaste/food_list.html",{"form":form})









 






