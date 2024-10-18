from rest_framework import  serializers
from asset.models import *
from portfolio.models import *

class portfolio_serializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ('user','title')
        
class asset_serializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields =()
