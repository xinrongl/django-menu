from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Dish
# Create your views here.


def index(request):
    dishes = Dish.objects.all()
    context = {
        "dishes": dishes
    }
    # return render(request, "app/index.html", context)
    return render(request, "index.html", context)


def details(request, dish_id):
    response = f"You're looking at results of dish: {dish_id}"
    image_path = Dish.objects.values_list("dish_image", flat=True)[0]
    
    return HttpResponse(response)
