from rest_framework import generics
from .models import Portfolio,PortfolioAsset
from asset.models import Asset
from .serializers import PortfolioSerializer,PortfolioAssetSerializer

class PortfolioListCreateView(generics.ListCreateAPIView):
    serializer_class = PortfolioSerializer

    def get_queryset(self):
        return Portfolio.objects.all()

    def perform_create(self, serializer):
        serializer.save()

class PortfolioDetailView(generics.RetrieveUpdateAPIView):
        serializer_class = PortfolioSerializer
        def get_queryset(self):

            return Portfolio.objects.all()

class PortfolioAssetListCreateView(generics.ListCreateAPIView):
    serializer_class = PortfolioAssetSerializer

    def get_queryset(self):
        return PortfolioAsset.objects.filter(portfolio_id=self.kwargs['portfolio_id'])

    def perform_create(self, serializer):
        serializer.save()

class PortfolioAssetDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = PortfolioAssetSerializer
    def get_queryset(self):
        portfolio_id = self.kwargs['portfolio_id']
        return PortfolioAsset.objects.filter(portfolio_id=portfolio_id)
    