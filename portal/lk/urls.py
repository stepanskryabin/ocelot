from django.urls import path

from . import views

app_name = 'lk'

urlpatterns = [
    path('login', views.user_login, name='user_login')
]
