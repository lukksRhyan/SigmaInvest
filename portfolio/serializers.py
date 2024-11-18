from rest_framework import serializers
from .models import Portfolio, PortfolioAsset, User


class PortfolioAssetSerializer(serializers.ModelSerializer):

    class Meta:
        model = PortfolioAsset
        fields = ['asset','portfolio','quantity','average_price']

class PortfolioSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    total = serializers.DecimalField(max_digits=15, decimal_places=7,read_only=True)
    appreciation = serializers.DecimalField(max_digits=15, decimal_places=7, read_only=True)
    followers = serializers.DecimalField(max_digits=10, decimal_places=0,read_only=True     )

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.total = validated_data.get('total', instance.total)
        instance.appreciation = validated_data.get('appreciation', instance.appreciation)
        instance.followers = validated_data.get('followers', instance.followers)
        instance.save()
        return instance

    def create(self, validated_data):
        username = validated_data.pop('user', None)
        user = User.objects.get(username=username)
        portfolio = Portfolio.objects.create(user = user,**validated_data)

        return portfolio

    class Meta:
        model = Portfolio
        fields = ['id','user','username','title', 'total', 'appreciation', 'followers']
