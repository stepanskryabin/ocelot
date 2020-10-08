from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate


def parser(request):
    return render(request, 'heat/home/parser.html')
