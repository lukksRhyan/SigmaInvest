from decimal import Decimal
from os.path import split

from django.utils import timezone
from django.conf import settings
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
import requests
import portfolio
from asset.models import Asset
from .models import Portfolio, PortfolioAsset, User, History


class PortfolioAssetSerializer(serializers.ModelSerializer):
    ticker = serializers.ReadOnlyField(source='asset.ticker')
    name = serializers.ReadOnlyField(source='asset.name')
    price = serializers.DecimalField(max_digits=10, decimal_places=2, write_only=True)
    average_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)


    class Meta:
        model = PortfolioAsset
        fields = ['asset', 'portfolio', 'price', 'name', 'ticker', 'quantity', 'average_price']

    def get_external_data(self,ticker):
        try:
            response = requests.get(f'https://brapi.dev/api/quote/{ticker}', params={'token': settings.API_KEY})
            response.raise_for_status()
            data = response.json()['results'][0]
            name = data['shortName'].split()[0]
            close = data.get("regularMarketPrice")
            logo = data.get('logourl')
            return name,close,logo
        except Exception as e:
            print(f"Erro ao buscar api externa: {e}")
            return None,None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        name,close, logo = self.get_external_data(instance.asset.ticker)
        if name is not None:
            representation['name'] = name
        if close is not None:
            representation['close'] = close
        if logo is not None:
            representation['logo'] = logo

        representation['stock'] = instance.asset.ticker
        return representation

    def update(self, instance, validated_data):
        price = validated_data.get('price')
        quantity = validated_data.get('quantity')

        if price is None or quantity is None:
            raise ValidationError({'detail': 'Price and quantity are required for update.'})

        instance.average_price = (instance.average_price * instance.quantity + price * quantity) / (instance.quantity + quantity)
        instance.quantity += quantity
        portfolio  = instance.portfolio()
        portfolio.total +=(price * quantity)
        portfolio.save()
        instance.save()
        return instance



class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['portfolio', 'asset', 'quantity', 'quotation']

    def create(self, validated_data):
        portfolio = validated_data.get('portfolio')
        stock = validated_data.get('asset')
        quantity = validated_data.get('quantity')
        quotation = validated_data.get('quotation')

        if quantity == 0 or quotation <= 0:
            raise ValidationError({'detail': 'Quantity and quotation must be positive values.'})

        # Buscar ou criar o ativo
        asset, _ = Asset.objects.get_or_create(ticker=stock)

        # Validar existência do portfolio
        if not Portfolio.objects.filter(id=portfolio.id).exists():
            raise ValidationError({'portfolio': 'Portfolio not found.'})

        # Calcular custo
        cost = Decimal(quantity) * Decimal(quotation)

        # Atualizar ou criar o ativo no portfolio
        portfolio_asset = PortfolioAsset.objects.filter(portfolio=portfolio, asset=asset).first()
        if portfolio_asset:
            #print(portfolio_asset)
            total_quantity = portfolio_asset.quantity + quantity
            if total_quantity <= 0:
                portfolio_asset.delete()
            total_cost = (portfolio_asset.quantity * portfolio_asset.average_price) + cost
            portfolio_asset.average_price = total_cost / total_quantity
            portfolio_asset.quantity = total_quantity
            portfolio = portfolio_asset.portfolio
            #print(portfolio)
            portfolio.total += total_cost
            print(portfolio.total)
            portfolio.save()
            portfolio_asset.save()
        else:
            PortfolioAsset.objects.create(
                portfolio=portfolio,
                asset=asset,
                quantity=quantity,
                average_price=quotation
            )
            portfolio.total += quantity*quotation
            portfolio.save()

        # Criar histórico
        history = History.objects.create(
            portfolio=portfolio,
            asset=asset,
            quantity=quantity,
            quotation=quotation,
            date=timezone.now()
        )
        return history


class PortfolioSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    appreciation = serializers.DecimalField(max_digits=15, decimal_places=2, read_only=True)
    followers = serializers.DecimalField(max_digits=10, decimal_places=0, read_only=True)

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
        portfolio = Portfolio.objects.create(user=user, **validated_data)
        return portfolio

    class Meta:
        model = Portfolio
        fields = ['id', 'user', 'username', 'title',  'appreciation', 'followers']

    def get_assets(self,obj):
        serialized_assets = PortfolioAssetSerializer(PortfolioAsset.objects.filter(portfolio=obj), many=True).data
        invested_subtotal = sum(float(asset['average_price']) * float(asset['quantity']) for asset in serialized_assets)
        current_subtotal = sum(float(asset['close']) * float(asset['quantity']) for asset in serialized_assets if 'close' in asset)

        return {
                'assets':serialized_assets,
            "invested": round(invested_subtotal, 2),
            "total": round(current_subtotal, 2),
                }
    def to_representation(self,instance):
        representation = super().to_representation(instance)
        assets_data = self.get_assets(instance)

        representation['assets'] = assets_data['assets']
        representation['invested'] = assets_data['invested']
        representation['total'] = assets_data['total']

        return representation
