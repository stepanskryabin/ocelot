from django.contrib import admin

from .models import ConsumptionODPU
from .models import ConsumptionApartmentIPU
from .models import ConsumptionHomeIPU
from .models import ConsumptionRSO
from .models import ResourceCharge


@admin.register(ConsumptionODPU)
class ConsumptionODPUView(admin.ModelAdmin):
    list_display = ("home", "resource_type", "time_record", "Q1", "M1", "M2")
    list_filter = ("home", "resource_type", "time_record", "Q1", "M1", "M2")
    search_fields = ("home", "resource_type", "time_record", "Q1", "M1", "M2")
    date_hierarchy = ("time_record")
    ordering = ("home", "resource_type", "time_record", "Q1", "M1", "M2")


@admin.register(ConsumptionApartmentIPU)
class ConsumptionApartmentIPUView(admin.ModelAdmin):
    list_display = ("home", "time_record", "apartment", "resource_type",
                    "IPU_indication", "IPU_consumption", "IPU_calories",
                    "recalculation_mass", "recalculation_calories")
    list_filter = ("home", "time_record", "apartment", "resource_type")
    search_fields = ("home", "time_record", "apartment", "resource_type")
    date_hierarchy = ("time_record")
    ordering = ("home", "time_record", "apartment", "resource_type")


@admin.register(ConsumptionHomeIPU)
class ConsumptionHomeIPUView(admin.ModelAdmin):
    list_display = ("home", "time_record", "resource_type",
                    "IPU_mass", "IPU_calories")
    list_filter = ("home", "time_record", "resource_type")
    search_fields = ("home", "time_record", "resource_type")
    date_hierarchy = ("time_record")
    ordering = ("home", "time_record", "resource_type")


@admin.register(ConsumptionRSO)
class ConsumptionRSOView(admin.ModelAdmin):
    list_display = ("home", "time_record", "ODPU_mass", "IPU_RP_mass",
                    "IPU_nonRP_mass", "ODN_mass", "negative_ODN_mass",
                    "result_ODN_mass", "payable_ODN_mass")
    list_filter = ("home", "time_record", "ODPU_mass", "IPU_RP_mass",
                   "IPU_nonRP_mass", "ODN_mass", "negative_ODN_mass",
                   "result_ODN_mass", "payable_ODN_mass")
    search_fields = ("home", "time_record", "ODPU_mass", "IPU_RP_mass",
                     "IPU_nonRP_mass", "ODN_mass", "negative_ODN_mass",
                     "result_ODN_mass", "payable_ODN_mass")
    date_hierarchy = ("time_record")
    ordering = ("home", "time_record", "ODPU_mass", "IPU_RP_mass",
                "IPU_nonRP_mass", "ODN_mass", "negative_ODN_mass",
                "result_ODN_mass", "payable_ODN_mass")


@admin.register(ResourceCharge)
class ResourceChargeView(admin.ModelAdmin):
    list_display = ("home", "time_record", "norm_mass", "norm_finance",
                    "accrued_mass", "accured_finance", "saldo_mass",
                    "saldo_finance", "payed", "tarif", "nalog")
    list_filter = ("home", "time_record", "norm_mass", "norm_finance",
                   "accrued_mass", "accured_finance", "saldo_mass",
                   "saldo_finance", "payed")
    search_fields = ("home", "time_record", "norm_mass")
    date_hierarchy = ("time_record")
    ordering = ("home", "time_record", "norm_mass", "norm_finance",
                "accrued_mass", "accured_finance", "saldo_mass",
                "saldo_finance", "payed")
