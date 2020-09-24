from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Home


def home_list(request):
    homes = Home.all()
    return render(request, 'heat/home/list.html', {'homes': homes})


def home_detail(request, adress):
    homes = get_object_or_404(Home, adress=adress)
    render(request, 'heat/home/detail.html', {'homes': homes})
