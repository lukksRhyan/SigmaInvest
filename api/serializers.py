from rest_framework import  serializers
from asset.models import *
from portfolio.models import *

class PortifolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ('user','title')
        
class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields =()
