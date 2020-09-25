from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Home


def home_list(request):
    homes = Home.objects.all()
    return render(request, 'heat/home/list.html', {'homes': homes})


def home_detail(request, home_number):
    homes = get_object_or_404(Home, home_number=home_number)
    return render(request, 'heat/home/detail.html', {'homes': homes})


def parser(request):
    pass
