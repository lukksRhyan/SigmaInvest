from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login

from portfolio.forms import UserRegisterForm


def userRegister(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserRegisterForm()

    return render(request, 'users/signup.html', {'form': form})
