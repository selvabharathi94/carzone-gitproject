from django.shortcuts import render
from .models import Car
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def cars(request):
    cars = Car.objects.all()
    paginator = Paginator(cars, 4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    return render(request, 'cars/cars.html', {'cars': paged_cars})


def car_detail(request, pk):
    car = Car.objects.get(id=pk)
    return render(request, 'cars/car_detail.html', {'car': car})
