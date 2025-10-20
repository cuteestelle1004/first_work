from django.http import HttpResponse  # Add this import
from django.shortcuts import render
from .models import Food

def home(request):
    return HttpResponse("buying food has never been easier!")

def rice(request):
    return render(request, 'rice.html')

def pasta(request):
    foods = Food.objects.filter(category='pasta')
    return render(request, 'pasta.html', {'foods': foods})

def price(request):
    foods = Food.objects.all()  # get all food items from the database
    return render(request, 'home.html', {'foods': foods})

