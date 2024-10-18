import requests
from urllib.parse import urljoin, urlencode


class ApiConnection:
    def __init__(self):
        self.base_url = 'https://brapi.dev/api/'
        self.token = "7AYrqS5jDLBXnrturQkFcj"

    def __str__(self):
        pass

    def construct_url(self,endpoint, params = None):
        url = urljoin(self.base_url, endpoint)
        if params is None:
            params = {}
        params['token'] = self.token
        query_string = urlencode(params)
        return f"{url}?{query_string}"

    def get_asset_data_by_ticker(self,ticker):
        endpoint = endpoint_by_classification("STOCK")
        params = {'symbol': ticker}
        response = requests.get(self.construct_url(endpoint,params))
        if response.status_code == 200:
            return response.json()
        return None

    def search_by_ticker(self,ticker)->list:
        endpoint = "list/"
        params = {'search': ticker}
        response = requests.get(self.construct_url(endpoint,params))
        if response.status_code == 200:
            return response.json()
        return []

def endpoint_by_classification(classification)->str:
    if classification == "STOCK":
      return "quote/"
    pass