from dbm import error

from django.conf import settings
import requests
from django.http import JsonResponse
from requests import Response
from rest_framework import generics
from .models import Asset, AssetSector, AssetClassification
from .serializers import AssetSerializer,AssetSectorSerializer,AssetClassificationSerializer

#Asset
class AssetListCreate(generics.ListCreateAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

    def get_queryset(self):
        return Asset.objects.all()

    def perform_create(self, serializer):
        serializer.save()

class AssetDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetSerializer

    def get_queryset(self):
        return Asset.objects.all()

#AssetSector
class AssetSectorListCreate(generics.ListCreateAPIView):
    queryset = AssetSector.objects.all()
    serializer_class = AssetSectorSerializer

    def get_queryset(self):
        return AssetSector.objects.all()

    def perform_create(self, serializer):
        serializer.save()

class AssetSectorDetail(generics.RetrieveUpdateDestroyAPIView):

    def get_queryset(self):
        return AssetSector.objects.all()

#AssetClassification
class AssetClassificationListCreate(generics.ListCreateAPIView):
    queryset = AssetClassification.objects.all()

    serializer_class = AssetClassificationSerializer
    def get_queryset(self):
        return AssetClassification.objects.all()

class AssetClassificationDetail(generics.RetrieveUpdateDestroyAPIView):

    def get_queryset(self):
        return AssetClassification.objects.all()


def asset_search(request) -> JsonResponse:
    '''Faz a busca utilizando um dos 3 tipos de ativos disponiveis na Brapi'''
    asset_type = request.GET.get('type')
    external_end_point = {
        'stock': 'quote/list',
        'crypto': 'v2/crypto/available',
        'currency': 'v2/currency/available'
    }
    request_url = f'https://brapi.dev/api/{external_end_point[asset_type]}'
    params ={
        'token': settings.API_KEY,
    }
    try:
        response = requests.get(request_url,params=params)
        response.raise_for_status()
    except Exception as e:
        return JsonResponse({'error': str(e)})
    data = response.json()
    response_keys = {
        'stock': 'stocks',
        'crypto': 'coins',
        'currency': 'currencies'
    }
    asset_key = response_keys.get(asset_type)
    if asset_key in data:
        return JsonResponse(data[asset_key], safe=False)
    return JsonResponse(data={'error':'Erro com a api externa'}, status=500)

def search_by_ticker(ticker) -> dict:
    url = ''
    pass

def crypto_data_fill() -> None:
    url = 'https://brapi.dev/api/v2/crypto/available'
    try:
        response = requests.get(url, params={'token': settings.API_KEY})
        response.raise_for_status()
    except Exception as e:
        return JsonResponse({'error': str(e)})
    data = response.json()
    for crypto in data:
        print(crypto)


