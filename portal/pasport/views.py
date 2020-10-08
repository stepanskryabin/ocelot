from django.shortcuts import render

from .models import Home
from .models import HomeApartment
from .models import HomeParametrs

from .forms import HomeForm
from .forms import HomeApartmentForm
from .forms import HomeParametrsForm


def home_list(request):
    homes = Home.objects.all()
    verbose_names = [field.verbose_name for field in homes[0]._meta.fields]
    names = [field.name for field in homes[0]._meta.fields]
    if request.method == 'POST':
        form = HomeForm(data=request.POST)
        if form.is_valid():
            form.save()
    else:
        form = HomeForm()
    result = {
        'elements': homes,
        "verbose_names": verbose_names,
        "names": names,
        "form": form
        }
    return render(request, 'heat/home.html', context=result)


def home_apartment_list(request):
    apartments = HomeApartment.objects.all()
    verbose_names = [field.verbose_name for field in apartments[0]._meta.fields]
    names = [field.name for field in apartments[0]._meta.fields]
    if request.method == 'POST':
        form = HomeApartmentForm(data=request.POST)
        if form.is_valid():
            form.save()
    else:
        form = HomeApartmentForm()
    result = {
        'elements': apartments,
        "verbose_names": verbose_names,
        "names": names,
        "form": form
        }
    return render(request, 'heat/homeapartment.html', context=result)


def home_parametrs_list(request):
    parametrs = HomeParametrs.objects.all()
    verbose_names = [field.verbose_name for field in parametrs[0]._meta.fields]
    names = [field.name for field in parametrs[0]._meta.fields]
    if request.method == 'POST':
        form = HomeParametrsForm(data=request.POST)
        if form.is_valid():
            form.save()
    else:
        form = HomeParametrsForm()
    result = {
        'elements': parametrs,
        "verbose_names": verbose_names,
        "names": names,
        "form": form
        }
    return render(request, 'heat/homeparametrs.html', context=result)
