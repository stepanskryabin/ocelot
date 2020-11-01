from django.contrib import admin

from .models import Odpu
from .models import ApartmentIpu
from .models import HomeIpu
from .models import Rso
from .models import ResourceOdn
from .models import ResourceChargeOdn


@admin.register(Odpu)
class OdpuView(admin.ModelAdmin):
    list_display = ("home",
                    "resource_type",
                    "time_record",
                    "temp1",
                    "temp2",
                    "temp3",
                    "g1",
                    "g2",
                    "work_time",
                    "idle_time",
                    "q1",
                    "q2",
                    "m1",
                    "m2",
                    "m3",
                    "m")
    list_filter = ("home",
                   "resource_type",
                   "time_record",
                   "m")
    search_fields = ("home",
                     "resource_type",
                     "time_record",
                     "m")
    date_hierarchy = ("time_record")
    ordering = ("home",
                "resource_type",
                "time_record")


@admin.register(ApartmentIpu)
class ApartmentIpuView(admin.ModelAdmin):
    list_display = ("home",
                    "time_record",
                    "apartment",
                    "resource_type",
                    "indication",
                    "consumption",
                    "calories",
                    "recalc_mass",
                    "recalc_calories")
    list_filter = ("home",
                   "time_record",
                   "apartment",
                   "resource_type",
                   "indication",
                   "consuption")
    search_fields = ("home",
                     "time_record",
                     "apartment",
                     "resource_type")
    date_hierarchy = ("time_record")
    ordering = ("home",
                "time_record",
                "apartment",
                "resource_type")


@admin.register(HomeIpu)
class HomeIpuView(admin.ModelAdmin):
    list_display = ("home",
                    "time_record",
                    "resource_type",
                    "mass",
                    "calories")
    list_filter = ("home",
                   "time_record",
                   "resource_type",
                   "mass")
    search_fields = ("home",
                     "time_record",
                     "resource_type")
    date_hierarchy = ("time_record")
    ordering = ("home",
                "time_record",
                "resource_type")


@admin.register(Rso)
class RsoView(admin.ModelAdmin):
    list_display = ("home",
                    "time_record",
                    "ODPU_mass",
                    "ODPU_calories",
                    "IPU_RP_mass",
                    "IPU_RP_mass",
                    "IPU_RP_calories",
                    "IPU_nonRP_mass",
                    "IPU_nonRP_calories",
                    "ODN_mass",
                    "ODN_calories",
                    "negative_ODN_mass",
                    "negative_ODN_calories",
                    "result_ODN_mass",
                    "result_ODN_calories",
                    "payable_ODN_mass",
                    "payable_ODN_calories")
    list_filter = ("home",
                   "time_record",
                   "ODPU_mass",
                   "IPU_RP_mass",
                   "IPU_nonRP_mass",
                   "ODN_mass",
                   "negative_ODN_mass",
                   "result_ODN_mass",
                   "payable_ODN_mass")
    search_fields = ("home",
                     "time_record",
                     "ODPU_mass",
                     "IPU_RP_mass",
                     "IPU_nonRP_mass",
                     "ODN_mass",
                     "negative_ODN_mass",
                     "result_ODN_mass",
                     "payable_ODN_mass")
    date_hierarchy = ("time_record")
    ordering = ("home",
                "time_record",
                "ODPU_mass",
                "IPU_RP_mass",
                "IPU_nonRP_mass",
                "ODN_mass",
                "negative_ODN_mass",
                "result_ODN_mass",
                "payable_ODN_mass")


@admin.register(ResourceOdn)
class ResourceOdnView(admin.ModelAdmin):
    list_display = ("home",
                    "time_record",
                    "odn_mass",
                    "odn_gkal")
    list_filter = ("home",
                   "time_record",
                   "odn_mass",
                   "odn_gkal")
    search_fields = ("home", "time_record")
    date_hierarchy = ("time_record")
    ordering = ("home",
                "time_record",
                "odn_mass",
                "odn_gkal")


@admin.register(ResourceChargeOdn)
class ResourceChargeOdnView(admin.ModelAdmin):
    list_display = ("home",
                    "time_record",
                    "mass",
                    "finance",
                    "payed",
                    "norm_mass",
                    "norm_finance",
                    "over_mass",
                    "over_finance"
                    "saldo_mass",
                    "saldo_finance")
    list_filter = ("home",
                   "time_record",
                   "mass",
                   "finance",
                   "payed",
                   "norm_mass",
                   "norm_finance",
                   "over_mass",
                   "over_finance"
                   "saldo_mass",
                   "saldo_finance")
    search_fields = ("home",
                     "time_record")
    date_hierarchy = ("time_record")
    ordering = ("home",
                "time_record",
                "mass",
                "finance",
                "payed",
                "norm_mass",
                "norm_finance",
                "over_mass",
                "over_finance"
                "saldo_mass",
                "saldo_finance")
