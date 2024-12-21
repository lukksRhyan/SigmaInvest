from rest_framework import serializers
from .models import Portfolio, PortfolioAsset, User, History


class PortfolioAssetSerializer(serializers.ModelSerializer):
    ticker = serializers.ReadOnlyField(source='asset.ticker')
    name = serializers.ReadOnlyField(source='asset.name')
    price = serializers.DecimalField(max_digits=10, decimal_places=2,write_only=True)
    average_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    def update(self, instance, validated_data):
        price = validated_data.pop('price')
        quantity = validated_data.pop('quantity')

        instance.average_price = validated_data.get('average_price', instance.average_price)

    class Meta:
        model = PortfolioAsset
        fields = ['asset','portfolio','price','name','ticker','quantity','average_price']

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['portfolio','asset','quantity','quotation']

    def create(self, validated_data):
        portfolio = validated_data['portfolio']
        asset = validated_data['asset']
        quantity = validated_data['quantity']
        quotation = validated_data['quotation']

        cost = quantity * quotation

        existing_asset = PortfolioAsset.objects.filter(portfolio=portfolio,asset=asset)
        if existing_asset:
            total_quantity = existing_asset.quantity + quantity
            total_cost = existing_asset.total + cost



        pass
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
