import requests

class ApiConnection:
    def __init__(self):
        self.base_url = 'https://brapi.dev/api/'
        self.token = "token="

    def construct_url(self,endpoint):
        return self.base_url + endpoint + self.token

    def get_asset_data_by_ticker(self,ticker):
        endpoint = "quote/?"
        response = requests.get(self.construct_url(endpoint))
        if response.status_code == 200:
            return response.json()
        return None


    def search_by_ticker(self,ticker)->list[str]:
        endpoint = "list/?search=" + ticker + "&"

        response = requests.get(self.construct_url(endpoint))
        if response.status_code == 200:
            return response.json()
        return [""]

