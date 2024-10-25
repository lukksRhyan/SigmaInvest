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





