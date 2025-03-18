from django.contrib.auth import get_user_model
from django.db import models
from django.utils.timezone import now

from portfolio.models import Portfolio, History

User = get_user_model()
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True, default="Investidor na SigmaInvest")
    user_since = models.DateTimeField(default=now)
    @property
    def user_portfolios(self):
        return Portfolio.objects.filter(user=self.user)

class Posting(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction = models.OneToOneField(History, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, blank=True, default="Movimentação realizada!")
    post_date = models.DateTimeField(default=now)
    likes = models.IntegerField(default=0)

class PostLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE)