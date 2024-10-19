from django.urls import path, include

urlpatterns =[
    path('portfolios/', include('portfolio.urls')),
]