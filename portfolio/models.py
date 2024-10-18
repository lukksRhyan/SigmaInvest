from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()
# Create your models here.
class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default=f"carteira de {user}")

    def __innit__(self,username,title):
        self.user = username
        self.title = title

    def __str__(self):
        return f"""
        Título da carteira: {self.title}
        Ativos: {[]}
        """

    def get_all_assets(self):
        return PortfolioAsset.objects.filter(portfolio=self)


class PortfolioAsset(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    ticker = models.CharField(max_length=10, null=True, blank=True)
    quantity =  models.DecimalField(max_digits=10, decimal_places=2)
    average_price = models.DecimalField(max_digits=10,decimal_places=2)


    def __str__(self):
        return f"total de {self.ticker} na {self.portfolio}"
