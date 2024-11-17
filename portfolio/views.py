from requests import Response
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
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


class PortfolioByUserView(generics.ListAPIView):
    serializer_class = PortfolioSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Portfolio.objects.filter(user=self.request.user.id)
    