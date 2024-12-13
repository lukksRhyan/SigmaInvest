
from django.conf import settings
import requests
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.views import APIView
from .models import Asset, AssetSector, AssetClassification
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
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


class GetStocksView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self,request):
        response = requests.get('https://brapi.dev/api/quote/list', params={'token':settings.API_KEY})
        stocks = response.json()['stocks']
        return JsonResponse(stocks, safe=False)

class GetStockDetail(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self,request):
        ticker = request.data['ticker']
        response = requests.get(f'https://brapi.dev/api/quote/{ticker}', params={'token':settings.API_KEY})

        if response.status_code == 200:
            stock = response.json()['results']
            return JsonResponse(stock, safe=False)
        return JsonResponse({'error':'erro ao contatar api externa'})


## DESCONTINUADO DEVIDO A NÃO FUNCIONAMENTO DA API |
#                                                  V
@DeprecationWarning
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
    if asset_type == 'currency': params.update({'search':'BR'})
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

@DeprecationWarning
def crypto_data_fill(request) -> JsonResponse:
    url = 'https://brapi.dev/api/v2/crypto/available'
    try:
        response = requests.get(url, params={'token': settings.API_KEY})
        response.raise_for_status()
    except Exception as e:
        return JsonResponse({'error': str(e)})
    coins = response.json()['coins']
    data= []
    for coin in coins:
        try:
            individual_response = requests.get(f'https://brapi.dev/api/v2/crypto/', params={'token': settings.API_KEY,'coin':coin})
            data.append(individual_response.json())
        except Exception as e:
            pass
    return JsonResponse(data, safe=False)


