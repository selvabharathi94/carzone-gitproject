from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.cars, name='cars'),
    re_path('(?P<pk>\d+)/$', views.car_detail, name='car_detail')
]
