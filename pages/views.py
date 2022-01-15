from django.shortcuts import render
from .models import Team

# Create your views here.


def home(request):
    teams_list = Team.objects.all()
    return render(request, 'pages/home.html', {'teams_list': teams_list})


def about(request):
    teams_list = Team.objects.all()
    return render(request, 'pages/about.html', {'teams_list': teams_list})


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    return render(request, 'pages/contact.html')
