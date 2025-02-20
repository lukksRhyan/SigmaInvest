from django.contrib.auth import get_user_model
from django.db import models
from django.utils.timezone import now

from portfolio.models import Portfolio
User = get_user_model()
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True, default="Investidor na SigmaInvest")
    user_since = models.DateTimeField(default=now)
    @property
    def user_portfolios(self):
        return Portfolio.objects.filter(user=self.user)