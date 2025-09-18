from django.shortcuts import render
from .models import Car

def home2(request):
    cars = Car.objects.all()
    return render(request, 'home2.html', {'cars': cars})

def drive(request):
    return render(request, 'home2.html')

