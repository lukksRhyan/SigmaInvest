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
    ticker = models.CharField(max_length=10, unique=True, null=False)
    sector = models.ForeignKey(AssetSector, on_delete=models.CASCADE, null=False)
    classification = models.ForeignKey(AssetClassification, on_delete=models.CASCADE, null=False)



    def __str__(self):
        return self.ticker

    def try_quote(self):
        pass
