from django.contrib import admin

from .models import Home
from .models import HomeApartment
from .models import HomeTechParametrs
from .models import HomeManagmentParameters
from .models import HomeNormativeParameters
from .models import HomeEconomicParameters


@admin.register(Home)
class HomeView(admin.ModelAdmin):
    list_display = ("created",
                    "updated",
                    "city",
                    "adress",
                    "home_number",
                    "home_sub_number")
    list_filter = ("created",
                   "updated",
                   "city",
                   "adress",
                   "home_number")
    search_fields = ("created",
                     "updated",
                     "city",
                     "adress",
                     "home_number")


@admin.register(HomeApartment)
class HomeApartmentView(admin.ModelAdmin):
    list_display = ("created",
                    "updated",
                    "home",
                    "number",
                    "apartment_type")
    list_filter = ("created",
                   "updated",
                   "home",
                   "number",
                   "apartment_type")
    search_fields = ("created",
                     "updated",
                     "home",
                     "number",
                     "apartment_type")


@admin.register(HomeTechParametrs)
class HomeTechParametrsView(admin.ModelAdmin):
    list_display = ("home",
                    "created",
                    "updated",
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
    list_filter = ("home",
                   "created",
                   "updated",
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
    search_fields = ("home",
                     "created",
                     "updated",
                     "year_building",
                     "entrances",
                     "elevators",
                     "floor",
                     "land_reg_number")


@admin.register(HomeManagmentParameters)
class HomeManagmentParametersViews(admin.ModelAdmin):
    list_display = ("home",
                    "contract_date",
                    "start_date",
                    "end_date")
    list_filter = ("home",
                   "contract_date",
                   "start_date",
                   "end_date")
    search_fields = ("home",
                     "contract_date",
                     "start_date",
                     "end_date")


@admin.register(HomeNormativeParameters)
class HomeNormativeParametersViews(admin.ModelAdmin):
    list_display = ("home",
                    "norm_hot_water",
                    "norm_cold_water",
                    "norm_preheating",
                    "norm_heating",
                    "norm_wastewater")
    list_filter = ("home",
                   "norm_hot_water",
                   "norm_cold_water",
                   "norm_preheating",
                   "norm_heating",
                   "norm_wastewater")
    search_fields = ("home",
                     "norm_hot_water",
                     "norm_cold_water",
                     "norm_preheating",
                     "norm_heating",
                     "norm_wastewater")


@admin.register(HomeEconomicParameters)
class HomeEconomicParametersViews(admin.ModelAdmin):
    list_display = ("home",
                    "tarif_hot_water",
                    "tarif_preheating",
                    "tarif_heating",
                    "tarif_cold_water",
                    "tarif_wastewater",
                    "nalog")
    list_filter = ("home",
                   "tarif_hot_water",
                   "tarif_preheating",
                   "tarif_heating",
                   "tarif_cold_water",
                   "tarif_wastewater",
                   "nalog")
    search_fields = ("home",
                     "tarif_hot_water",
                     "tarif_preheating",
                     "tarif_heating",
                     "tarif_cold_water",
                     "tarif_wastewater",
                     "nalog")
