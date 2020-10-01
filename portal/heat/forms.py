from django import forms

from .models import Home
from .models import HomeApartment
from .models import HomeParametrs


class HomeForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = ('city', 'adress',
                  'home_number', 'home_sub_number')


class HomeApartmentForm(forms.ModelForm):
    class Meta:
        model = HomeApartment
        fields = ('home', 'number', 'apartment_type')


class HomeParametrsForm(forms.ModelForm):
    class Meta:
        model = HomeParametrs
        fields = ('home', 'MOP', 'norm_cold_water',
                  'norm_hot_water', 'norm_heating')
