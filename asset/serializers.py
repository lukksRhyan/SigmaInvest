from rest_framework import serializers
from .models import Asset,AssetSector,AssetClassification

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ['id','ticker','sector_id','classification_id']

class AssetSectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetSector
        fields = ['sector']

class AssetClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetClassification
        fields = ['classification']
