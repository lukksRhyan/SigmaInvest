from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from user import views as user_views
from user.views import CustomLoginView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login') ,
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('signup/', user_views.user_register, name='signup'),
    path('index/', user_views.main_page, name='index'),
    path('authenticate/', CustomLoginView.as_view(), name='authenticate'),

    path('api/',include('api.urls')),
]
