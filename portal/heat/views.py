from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Home


def home_list(request):
    homes = Home.objects.all()
    test = dir(homes[0])
    return render(request, 'heat/home/list.html', {'homes': homes,
                                                    "test": test})


def parser(request):
    return render(request, 'heat/home/parser.html')
