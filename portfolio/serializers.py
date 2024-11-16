from rest_framework import serializers
from .models import Portfolio,PortfolioAsset

class PortfolioAssetSerializer(serializers.ModelSerializer):

    class Meta:
        model = PortfolioAsset
        fields = ['asset','portfolio','quantity','average_price']

class PortfolioSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username',read_only=True)
    total = serializers.DecimalField(max_digits=10, decimal_places=2)
    appreciation = serializers.DecimalField(max_digits=10, decimal_places=2)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.total = validated_data.get('total', instance.total)
        instance.appreciation = validated_data.get('appreciation', instance.appreciation)
        instance.followers = validated_data.get('followers', instance.followers)
        instance.save()
        return instance
    class Meta:
        model = Portfolio
        fields = ['id','user','title', 'total', 'appreciation', 'followers']
