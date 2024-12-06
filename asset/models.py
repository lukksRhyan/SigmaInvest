from django.db import models
import requests
import asset.api_connection as api
# Create your models here.
class AssetSector(models.Model):
    sector = models.CharField(max_length=10, unique=True, null=False)

    def __str__(self):
        return self.sector


class AssetClassification(models.Model):
    classification = models.CharField(max_length=10, unique=True, null=False)

    def __str__(self):
        return self.classification

class Asset(models.Model):
    ticker = models.CharField(max_length=10, unique=True, null=False)# Equivalente a coin para cripto e currency para moedas
    fullname = models.CharField(max_length=10, unique=True, null=True)
    classification = models.ForeignKey(AssetClassification, on_delete=models.CASCADE, null=True)



    def __str__(self):
        return self.ticker

    def try_quote(self):
        pass

class Stock(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE,default=1)

