from django.urls import path

import portfolio
from .views import *

urlpatterns =[
    path('', PortfolioListCreateView.as_view(), name='portfolio-list-create'),
    path('<int:pk>/', PortfolioDetailView.as_view(), name='portfolio-detail'),

    path('<int:pk>/assets', PortfolioAssetListCreateView.as_view(), name='portfolio-asset-list-create'),
    path('<int:pk>/assets', PortfolioAssetDetailView.as_view(), name='portfolio-asset-detail'),
]