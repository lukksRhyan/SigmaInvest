from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import Portfolio
from assets import api_connection
from portfolio.forms import UserRegisterForm

def main_page(request):
    if request.user.is_authenticated:
        info:dict = {}
        info.update({'username': request.GET.get('username')})
        token = api_connection.ApiConnection().token
        return render(request,'index.html',{'username':request.user.username,"token":token},)

    return redirect('login')

def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Portfolio.objects.create(username=user.username)
            login(request, user)
            return redirect('/')
    else:
        form = UserRegisterForm()

    return render(request, 'users/signup.html', {'form': form})
