from django.contrib import admin

from .models import Home
from .models import HomeApartment
from .models import HomeParametrs


@admin.register(Home)
class HomeView(admin.ModelAdmin):
    list_display = ("city", "adress", "home_number", "home_sub_number")
    list_filter = ("city", "adress", "home_number")
    search_fields = ("city", "adress", "home_number")
    ordering = ("adress", "home_number")


@admin.register(HomeApartment)
class HomeApartmentView(admin.ModelAdmin):
    list_display = ("home", "number", "apartment_type")
    list_filter = ("home", "number", "apartment_type")
    search_fields = ("home", "number", "apartment_type")
    ordering = ("home", "number", "apartment_type")


@admin.register(HomeParametrs)
class HomeParametrsView(admin.ModelAdmin):
    list_display = ("home", "MOP", "norm_cold_water",
                    "norm_hot_water", "norm_heating")
    list_filter = ("home", "MOP", "norm_cold_water",
                   "norm_hot_water", "norm_heating")
    search_fields = ("home", "MOP", "norm_cold_water",
                     "norm_hot_water", "norm_heating")
    ordering = ("home", "MOP", "norm_cold_water",
                "norm_hot_water", "norm_heating")
