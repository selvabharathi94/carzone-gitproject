from django.shortcuts import render
from .models import Car

# Create your views here.


def cars(request):
    cars = Car.objects.all()
    return render(request, 'cars/cars.html', {'cars': cars})


def car_detail(request, pk):
    car = Car.objects.get(id=pk)
    return render(request, 'cars/car_detail.html', {'car': car})
