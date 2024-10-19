from rest_framework import generics, permissions
from .models import Portfolio,PortfolioAsset
from .serializers import PortfolioSerializer,PortfolioAssetSerializer

class PortfolioListCreateView(generics.ListCreateAPIView):
    serializer_class = PortfolioSerializer

    def get_queryset(self):
        return Portfolio.objects.filter(user=self.request.POST.get('user'))

    def perform_create(self, serializer):
        serializer.save(user=self.request.POST.get('user'))

class PortfolioDetailView(generics.RetrieveUpdateAPIView):
        serializer_class = PortfolioSerializer

        def get_queryset(self):
            return Portfolio.objects.filter(user=self.request.POST.get('user'))

class PortfolioAssetListCreateView(generics.ListCreateAPIView):
    serializer_class = PortfolioAssetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        portfolio_id = self.kwargs['portfolio_id']
        return PortfolioAsset.objects.filter(portfolio_id=portfolio_id)

    def perform_create(self, serializer):
        portfolio = Portfolio.objects.get(id=self.kwargs['portfolio_id'])
        serializer.save(portfolio=portfolio)

class PortfolioAssetDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = PortfolioAssetSerializer
    def get_queryset(self):
        portfolio_id = self.kwargs['portfolio_id']
        return PortfolioAsset.objects.filter(portfolio_id=portfolio_id)
    