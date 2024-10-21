from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from portfolio.models import Portfolio
from asset import api_connection
from portfolio.forms import UserRegisterForm


def main_page(request):
    if request.user.is_authenticated:
        portfolios = Portfolio.objects.filter(user=request.user)

        assets = []
        for result in portfolios:
            assets.append(result.get_all_assets())
        token = api_connection.ApiConnection().token
        return render(request,'index.html',{'user':request.user,"token":token,'portfolios':portfolios},)

    return redirect('login')

def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)
            return render(request, 'index.html', {'user': user, "token": "token", 'portfolios': [portifolio]}, )

    else:
        form = UserRegisterForm()

    return render(request, 'users/signup.html', {'form': form})

