from django.shortcuts import render
from .models import Food, Donators
from django.shortcuts import render
from .models import Food, Donators
from .forms import CreateNewListing, FilterFoodList, DonatorRegistration
from django.shortcuts import redirect
from django.contrib import messages


def index(request):
    return render(request, 'PickMyWaste/index.html', {})


def home(response):
    return render(response, "PickMyWaste/home.html", {}) 


#function for form food listing
def create(request): 
    if request.method == "POST": 
        form = CreateNewListing(request.POST)
        if form.is_valid(): 
            donator = form.cleaned_data["donator"]
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            expiration_date = form.cleaned_data["expiration_date"]
            prepackaged = form.cleaned_data["prepackaged"]
            messages.success(request, "Profile updated successfully! Thank you for contributing.")
            
            t = Food(donator=donator, title=title, description= description, expiration_date = expiration_date, prepackaged = prepackaged) 
           
            t.save() 
         
   
            return redirect('view_food', id = t.id)

    else:
        form = CreateNewListing()
    return render(request,"PickMyWaste/create.html",{"form":form})


def view_food(request, id):
    food = Food.objects.get(id=id)
    return render (request,"PickMyWaste/food_view.html",{"food":food})



def list_food(response):
    if response.method == "GET": 
        form = FilterFoodList(response.GET)
        if form.is_valid():
            donator = form.cleaned_data["donator"]
            ls = Donators.objects.get(id = donator.id)
            food_list = Food.objects.filter(donator = ls)
            
            return render(response,"PickMyWaste/food_list.html",{"object_list":food_list, "form":form, "donor": ls})
    else:
         form = FilterFoodList()
    return render(response,"PickMyWaste/food_list.html",{"form":form})


def register(request):
    if request.method == "POST": 
        form = DonatorRegistration(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            address= form.cleaned_data["address"]
            city=form.cleaned_data["city"]
            state=form.cleaned_data["state"]
            zipcode=form.cleaned_data["zipcode"]
            phone= form.cleaned_data["phone"]
            email = form.cleaned_data["email"]
            messages.success(request, "Registration created successfully!")
            t = Donators(name=name, address=address, city=city, state=state, zipcode=zipcode, email=email, phone=phone)

            t.save()


    else:
        form = DonatorRegistration()
    return render(request,"PickMyWaste/register.html",{"form":form})








           
        










 






