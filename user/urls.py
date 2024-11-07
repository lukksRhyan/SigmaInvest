from django.urls import path

from .views import *

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', CustomRegisterView.as_view(), name='signup'),
    path('getdata/', UserDetailView.as_view(), name='getdata'),
]