from django.db import models

# Create your models here.
class Asset(models.Model):
    ASSET_TYPES = [
        ('stock', 'Ação'),
        ('crypto', 'Criptomoeda'),
        ('bond', 'Título'),
        ('real_estate', 'Fundo Imobilia'),
    ]
    name = models.CharField(max_length=100)
    ticker = models.CharField(max_length=10)
    type = models.CharField(choices=ASSET_TYPES, max_length=20)
    sector = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return f"{self.name} {self.ticker}"


