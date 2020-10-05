from django.urls import path

from . import views

app_name = 'heat'

urlpatterns = [
    path('home', views.home_list, name='post_list'),
    path('parser', views.parser, name='parser'),
    path('home-apartment', views.home_apartment_list, name='Home Apartment'),
    path('home-parametrs', views.home_parametrs_list, name='Home Parametrs'),
    path('admin', views.user_login, name='User login')
]
