from django.urls import path

from .views import *

urlpatterns = [
    path('', AssetListCreate.as_view(), name='asset-list-create'),
    path('<int:pk>/', AssetDetail.as_view(), name='asset-detail'),
    path('sector/', AssetSectorListCreate.as_view(), name='asset-sector-list-create'),
    path('sector/<int:pk>/', AssetSectorDetail.as_view(), name='asset-sector-detail'),
    path('classification/',AssetClassificationListCreate.as_view(), name='asset-classification-list-create'),
    path('classification/<int:pk>/', AssetClassificationDetail.as_view(), name='asset-classification-detail'),
    path('search/', asset_search, name='asset-search'),
    path('fill-crypto/', crypto_data_fill, name='crypto-data-fill'),

]