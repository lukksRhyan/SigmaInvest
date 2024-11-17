from django.urls import path

import portfolio
from .views import *

urlpatterns =[
    path('', PortfolioListCreateView.as_view(), name='portfolio-list-create'),
    path('<int:pk>/', PortfolioDetailView.as_view(), name='portfolio-detail'),
    path('<int:portfolio_id>/assets', PortfolioAssetListCreateView.as_view(), name='portfolio-asset-list-create'),
    path('<int:portfolio_id>/assets', PortfolioAssetDetailView.as_view(), name='portfolio-asset-detail'),
    path('byuser/',PortfolioByUserView.as_view(), name='portfolio-by-user')
]