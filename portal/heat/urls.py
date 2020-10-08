from django.urls import path

from . import views

app_name = 'heat'

urlpatterns = [
    path('parser', views.parser, name='parser')
]
