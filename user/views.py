from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from portfolio.models import Portfolio, User
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
            return render(request, 'index.html', {'user': user, "token": "token", 'portfolios': [Portfolio()]}, )

    else:
        form = UserRegisterForm()

    return render(request, 'users/signup.html', {'form': form})

class CustomLoginView(APIView):
    def post(self, request,*args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            token = Token.objects.get_or_create(user=user)
            return Response({'token':token.key})
        return Response({'error':'Invalid Credentials'}, status=400)

class CustomRegisterView(APIView):
    def post(self, request,*args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")

        if not all([username,password,email]):
            return Response({'error':'Preencha todos os campos'}, status=400)
        if User.objects.filter(username=username).exists():
            return Response({'error':'Usuário já cadastrado'}, status=400)

        user = User.objects.create_user(username=username, password=password, email=email)

        token,created = Token.objects.get_or_create(user=user)

        return Response({'token':token.key}, status=201 )

class UserDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        user_data= {
            "id":user.id,
            "username":user.username,
            "email":user.email,
        }
        return Response(user_data)
