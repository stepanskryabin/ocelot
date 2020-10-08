from django.urls import path

from . import views

app_name = 'pasport'

urlpatterns = [
    path('home', views.home_list, name='post_list'),
    path('home-apartment', views.home_apartment_list, name='Home Apartment'),
    path('home-parametrs', views.home_parametrs_list, name='Home Parametrs')
]