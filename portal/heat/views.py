from django.shortcuts import render
from django.http import HttpResponse


def parser(request):
    return render(request, 'heat/home/parser.html')
