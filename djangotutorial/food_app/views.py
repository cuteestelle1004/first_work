from django.http import HttpResponse  # Add this import
from django.shortcuts import render
from .models import Food

def home(request):
    return HttpResponse("buying food has never been easier!")

def sleep(request):
    return HttpResponse("Welcome to the Food App!")


def price(request):
    foods = Food.objects.all()  # get all food items from the database
    return render(request, 'home.html', {'foods': foods})

