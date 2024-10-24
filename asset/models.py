from django.db import models
import requests
import asset.api_connection as api
# Create your models here.
class AssetSector(models.Model):
    sector = models.CharField(max_length=10, unique=True, null=False)
    def __init__(self, sector):
        self.sector = sector.upper()

class AssetClassification(models.Model):
    classification = models.CharField(max_length=10, unique=True, null=False)
    def __init__(self, classification):
        self.classification = classification.upper()

class Asset(models.Model):
    ticker = models.CharField(max_length=10, unique=True, null=False)
    sector = models.ForeignKey(AssetSector, on_delete=models.CASCADE, null=False)
    classification = models.ForeignKey(AssetClassification, on_delete=models.CASCADE, null=False)

    def __init__(self, ticker, sector, classification):
        self.ticker = ticker.upper()
        self.sector = sector.upper()
        self.classification = classification.upper()
        self.data = api.ApiConnection().get_asset_data_by_ticker(ticker)

    def try_quote(self):
        pass
