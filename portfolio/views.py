from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import Portfolio,PortfolioAsset,History
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

    def perform_create(self, serializer):#Como eu altero este método para chamar o History.save()?
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

class CreatePortfolioView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        user = request.user
        title = request.data.get('title', f'carteira de {user}')

        portfolio = Portfolio.objects.create(user=user,title=title)

        serializer = PortfolioSerializer(portfolio)

        return Response(serializer.data, status=status.HTTP_201_CREATED)