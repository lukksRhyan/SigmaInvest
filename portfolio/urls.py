from django.urls import path

import portfolio
from .views import *

urlpatterns =[
    path('api/portfolios/', PortfolioListCreateView.as_view(), name='portfolio-list-create'),
    path('api/portfolios/<int:pk>/', PortfolioDetailView.as_view(), name='portfolio-detail'),

    path('api/portfolios/<int:pk>/assets', PortfolioAssetListCreateView.as_view(), name='portfolio-asset-list-create'),
    path('api/portfolios/<int:pk>/assets', PortfolioAssetDetailView.as_view(), name='portfolio-asset-detail'),
]