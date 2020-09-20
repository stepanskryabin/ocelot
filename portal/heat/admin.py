from django.contrib import admin
from .models import Home
from .models import HomeApartment
from .models import HomeParametrs
from .models import ConsumptionODPU
from .models import ConsumptionIPU
from .models import ConsumptionRSO
from .models import ResourceCharge


admin.site.register(Home)
admin.site.register(HomeApartment)
admin.site.register(HomeParametrs)
admin.site.register(ConsumptionODPU)
admin.site.register(ConsumptionIPU)
admin.site.register(ConsumptionRSO)
admin.site.register(ResourceCharge)
