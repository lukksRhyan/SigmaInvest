from decimal import Decimal

from django.contrib.auth import get_user_model
from django.db import models
from asset.models import Asset

User = get_user_model()

class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=15, decimal_places=7, default=0.0)
    appreciation = models.DecimalField(max_digits=15, decimal_places=7, default=0.0)
    title = models.CharField(max_length=100, default=f"carteira")
    followers = models.DecimalField(max_digits=10,decimal_places=0,default=0)

    def save(self,*args,**kwargs):
        if not self.title:
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

    def total(self) -> Decimal:
        return self.quantity * self.average_price

    def __str__(self):
        return f"{self.asset}@{self.portfolio}"

    def save(self, *args,quantity=0.0, quotation=0.0, **kwargs):
        existing_asset = PortfolioAsset.objects.filter(portfolio=self.portfolio,asset=self.asset).first()

        if existing_asset:
            total_quantity = existing_asset.quantity + self.quantity
            total_cost = (existing_asset.average_price * existing_asset.quantity) + (self.average_price * self.quantity)
            new_average_price = total_cost / total_quantity

            existing_asset.quantity = self.quantity
            PortfolioAsset.objects.filter(portfolio=self.portfolio,asset=self.asset).update(
                average_price=new_average_price,
                quantity = total_quantity
            )
        else:
            super().save(*args, **kwargs)

        transaction_history = History.objects.create(
            self.portfolio,
            self.asset,
            quantity,
            quotation,
        )

class Following(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    portfolio = models.ForeignKey(Portfolio, on_delete= models.CASCADE)
    followed_at = models.DateTimeField(auto_now_add=True)

class History(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete= models.CASCADE, default=1)
    date = models.DateField(auto_now_add=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    quotation = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def total (self) -> Decimal:
        return self.quantity * self.quotation
