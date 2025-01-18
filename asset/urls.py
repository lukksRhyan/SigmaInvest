from django.urls import path

from .views import *

urlpatterns = [
    path('', AssetListCreate.as_view(), name='asset-list-create'),
    path('<int:pk>/', AssetDetail.as_view(), name='asset-detail'),

    path('stocks', GetStocksView.as_view(), name='asset-stocks'),
    path('stocks/detail/', GetStockDetail.as_view(), name='stock-info'),

]