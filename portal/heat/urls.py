from django.urls import path

from . import views

app_name = 'heat'

urlpatterns = [
    path('', views.home_list, name='post_list'),
    path('parser', views.parser, name='parser')
]
