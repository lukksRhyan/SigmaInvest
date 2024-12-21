from decimal import Decimal

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.timezone import now

from asset.models import Asset

User = get_user_model()

class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=15, decimal_places=7, default=0.0)
    appreciation = models.DecimalField(max_digits=15, decimal_places=7, default=0.0)
    title = models.CharField(max_length=100, default=f"carteira")
    followers = models.DecimalField(max_digits=10,decimal_places=0,default=0)

    def save(self,*args,**kwargs):
        if not self.title and self.user.id:
            self.title = f'carteira de {self.user}'
        super().save(*args,**kwargs)


    def __str__(self):
        return f"{self.title}@{self.user}"

    def get_all_assets(self):
        return PortfolioAsset.objects.filter(portfolio=self)


class PortfolioAsset(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete= models.CASCADE)
    quantity =  models.DecimalField(max_digits=10, decimal_places=2)
    average_price = models.DecimalField(max_digits=10,decimal_places=2)
    @property
    def total(self) -> Decimal:
        return self.quantity * self.average_price

    def __str__(self):
        return f"{self.asset}@{self.portfolio}"

class Following(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    portfolio = models.ForeignKey(Portfolio, on_delete= models.CASCADE)
    followed_at = models.DateTimeField( default=now)

class History(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete= models.CASCADE, default=1)
    date = models.DateField(auto_now_add=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    quotation = models.DecimalField(max_digits=10, decimal_places=2)
    @property
    def total (self) -> Decimal:
        return self.quantity * self.quotation