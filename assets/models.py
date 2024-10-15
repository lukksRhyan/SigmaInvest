from django.db import models
import requests
import assets.api_connection as api
# Create your models here.
class Assets:

    def __init__(self, ticker):
        self.ticker = ticker.upper()
        self.data = api.ApiConnection().get_asset_data_by_ticker(ticker)




    def try_quote(self):
        pass
