from django.shortcuts import render
from .models import Food, Donators

from django.shortcuts import render, get_object_or_404

from .models import Food, Donators

from .forms import CreateNewListing, FilterFoodList, DonatorRegistration
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic.list import ListView
# from django.contrib import messages




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


# def detail(request, donator_id):
   
#     donator = get_object_or_404(Donators, pk=donator_id)
#     return render(request, 'PickMyWaste/.html', {'donator': donator})

def foodMap(response):
    return render(response,"PickMyWaste/foodMap.html")

#function for form food listing
def create(response): 
    if response.method == "POST": 
        form = CreateNewListing(response.POST)
        if form.is_valid(): 
            donator = form.cleaned_data["donator"]
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            expiration_date = form.cleaned_data["expiration_date"]
            prepackaged = form.cleaned_data["prepackaged"]
            # messages.success(request, "Profile updated successfully!")
            
            t = Food(donator=donator, title=title, description= description, expiration_date = expiration_date, prepackaged = prepackaged) 
           
            t.save() 
         
        # redirect the page to the id of the foodlisting
            return redirect('view_food', id = t.id)

    else:
        form = CreateNewListing()#create a blank form and pass to HTML
    return render(response,"PickMyWaste/create.html",{"form":form})

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
        if form.is_valid():
            donator = form.cleaned_data["donator"]
            ls = Donators.objects.get(id = donator.id)
            food_list = Food.objects.filter(donator = ls)
            
            return render(response,"PickMyWaste/food_list.html",{"object_list":food_list, "form":form, "donor": ls})
    else:
         form = FilterFoodList()
    return render(response,"PickMyWaste/food_list.html",{"form":form})

def register(response):
    if response.method == "POST": 
        form = DonatorRegistration(response.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            address= form.cleaned_data["address"]
            # phone= form.cleaned_data["phone"]
            email = form.cleaned_data["email"]
            
            t = Donators(name=name, address=address, email=email)

            t.save()

            return redirect('view_register', id = t.id)
            # return HttpResponseRedirect('/home/')

        else:
            form = DonatorRegistration()
        return render(response,"PickMyWaste/register.html",{"form":form})

# def view_register(request):
#     register = Donators.objects.get(id=id)
#     return render (request,"PickMyWaste/register.html",{"register":register})




            
            

#  name = models.CharField(max_length=100, blank=False, default='')
#     address = models.CharField(max_length=300, default='')
#     phone = PhoneNumberField(null=False, blank=False, unique=True)
#     email=models.EmailField(max_length=254, default='')


# def register(response):
#     return render(response,"PickMyWaste/register.html")









 






