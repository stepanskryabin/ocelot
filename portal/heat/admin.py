from django.contrib import admin

from .models import ConsumptionODPU
from .models import ConsumptionIPU
from .models import ConsumptionRSO
from .models import ResourceCharge


@admin.register(ConsumptionODPU)
class ConsumptionODPUView(admin.ModelAdmin):
    list_display = ("home", "resource_type", "time_record", "Q1", "M1", "M2")
    list_filter = ("home", "resource_type", "time_record", "Q1", "M1", "M2")
    search_fields = ("home", "resource_type", "time_record", "Q1", "M1", "M2")
    date_hierarchy = ("time_record")
    ordering = ("home", "resource_type", "time_record", "Q1", "M1", "M2")


@admin.register(ConsumptionIPU)
class ConsumptionIPUView(admin.ModelAdmin):
    list_display = ("home", "time_record", "apartment",
                    "IPU_mass", "recalculation_mass")
    list_filter = ("home", "time_record", "apartment",
                   "IPU_mass", "recalculation_mass")
    search_fields = ("home", "time_record", "apartment",
                     "IPU_mass", "recalculation_mass")
    date_hierarchy = ("time_record")
    ordering = ("home", "time_record", "apartment",
                "IPU_mass", "recalculation_mass")


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
    list_display = ("home", "time_record", "normative", "tarif", "nalog")
    list_filter = ("home", "time_record", "normative", "tarif", "nalog")
    search_fields = ("home", "time_record", "normative", "tarif", "nalog")
    date_hierarchy = ("time_record")
    ordering = ("home", "time_record", "normative", "tarif", "nalog")
