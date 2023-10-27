import requests
from decouple import config

request_key = config('request_key',default='')
request_params = {'access_key': request_key}


request = requests.get('http://api.exchangeratesapi.io/v1/latest', params=request_params).json()

class ExchangeRate:
    
    def __init__(self):
        self.key = config('request_key',default='')
        self.value = round(request['rates']['RUB']/request['rates']['CNY'], 1)
        
    def get_value(self):
        return self.value