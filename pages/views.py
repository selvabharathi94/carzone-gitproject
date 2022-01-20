from django.shortcuts import render
from .models import Team
from cars.models import Car

# Create your views here.


def home(request):
    teams_list = Team.objects.all()
    featured_cars = Car.objects.filter(is_featured=True)
    cars = Car.objects.all()
    return render(request, 'pages/home.html', {'teams_list': teams_list, 'featured_cars': featured_cars, 'cars': cars})


def about(request):
    teams_list = Team.objects.all()
    return render(request, 'pages/about.html', {'teams_list': teams_list})


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    return render(request, 'pages/contact.html')
