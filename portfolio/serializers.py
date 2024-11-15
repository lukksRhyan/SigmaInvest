from rest_framework import serializers
from .models import Portfolio,PortfolioAsset

class PortfolioAssetSerializer(serializers.ModelSerializer):

    class Meta:
        model = PortfolioAsset
        fields = ['asset','portfolio','quantity','average_price']

class PortfolioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Portfolio
        fields = ['id','user','title','total','appreciation']


