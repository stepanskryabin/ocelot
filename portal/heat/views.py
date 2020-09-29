from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Home


def home_list(request):
    homes = Home.objects.all()
    verbose_names = [field.verbose_name for field in homes[0]._meta.fields]
    names = [field.name for field in homes[0]._meta.fields]
    result = {
        'homes': homes,
        "verbose_names": verbose_names,
        "names": names
        }
    return render(request, 'heat/home/list.html', context=result)


def parser(request):
    return render(request, 'heat/home/parser.html')
