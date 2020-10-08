from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate

from .forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(request, username=cleaned_data['username'],
                                password=cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('OK')
                else:
                    return HttpResponse('BAD')
            else:
                return HttpResponse('INVALID')
    else:
        form = LoginForm()
    return render(request, 'heat/auth.html', {'form': form})
