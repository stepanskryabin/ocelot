from django.contrib import admin

from .models import Home
from .models import HomeApartment
from .models import HomeTechParametrs
from .models import HomeManagmentParameters
from .models import HomeNormativeParameters
from .models import HomeEconomicParameters


@admin.register(Home)
class HomeView(admin.ModelAdmin):
    list_display = ("city",
                    "adress",
                    "home_number",
                    "home_sub_number")
    list_filter = ("city",
                   "adress",
                   "home_number")
    search_fields = ("city",
                     "adress",
                     "home_number")
    ordering = ("adress",
                "home_number")


@admin.register(HomeApartment)
class HomeApartmentView(admin.ModelAdmin):
    list_display = ("home",
                    "number",
                    "apartment_type")
    list_filter = ("home",
                   "number",
                   "apartment_type")
    search_fields = ("home",
                     "number",
                     "apartment_type")
    ordering = ("home",
                "number",
                "apartment_type")


@admin.register(HomeTechParametrs)
class HomeTechParametrsView(admin.ModelAdmin):
    list_display = ("home",
                    "year_building",
                    "entrances",
                    "elevators",
                    "floor",
                    "living_room",
                    "non_living_room",
                    "square_full",
                    "square_living",
                    "square_non_living",
                    "square_cleaning",
                    "square_mop",
                    "square_land_area",
                    "land_reg_number")
    list_filter =  ("home",
                    "year_building",
                    "entrances",
                    "elevators",
                    "floor",
                    "living_room",
                    "non_living_room",
                    "square_full",
                    "square_living",
                    "square_non_living",
                    "square_cleaning",
                    "square_mop",
                    "square_land_area",
                    "land_reg_number")
    search_fields =  ("home",
                    "year_building",
                    "entrances",
                    "elevators",
                    "floor",
                    "land_reg_number")
    ordering =  ("home",
                 "year_building",
                 "entrances",
                 "elevators",
                 "floor",
                 "living_room",
                 "non_living_room",
                 "square_full",
                 "square_living",
                 "square_non_living",
                 "square_cleaning",
                 "square_mop",
                 "square_land_area",
                 "land_reg_number")
