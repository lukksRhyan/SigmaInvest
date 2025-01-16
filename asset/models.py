from django.db import models
import requests
import asset.api_connection as api
# Create your models here.
class Asset(models.Model):
    ticker = models.CharField(max_length=10, unique=True, null=False)# Equivalente a coin para cripto e currency para moedas
    fullname = models.CharField(max_length=10, unique=True, null=True)
    sector = models.CharField(max_length=30, default='Undefined')

    def __str__(self):
        return self.ticker

    def try_quote(self):
        pass
