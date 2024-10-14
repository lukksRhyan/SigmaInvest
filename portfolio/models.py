from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()
# Create your models here.
class Portfolio(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Carteira de {self.username}"

class PortfolioAsset(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    ticker = models.CharField(max_length=10)
    quantity =  models.DecimalField(max_digits=10, decimal_places=2)
    average_price = models.DecimalField(max_digits=10,decimal_places=2)


    def __str__(self):
        return f"total de {self.ticker} na {self.portfolio}"
