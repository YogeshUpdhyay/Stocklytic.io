from requests.models import Response
from config import TestConfig as config
import requests
import json
import datetime

class Stock:
    def __init__(self) -> None:
        self.base_url = config.BASE_URL

    def get_data(self, symbol, size = "full", function = "TIME_SERIES_DAILY_ADJUSTED"):
        # get data

        # defining parmas for the api request
        params = {
            'function': function,
            'outputsize': size,
            'symbol': symbol,
            'apikey': config.API_KEY
        }

        # making the api request and parsing the data
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            data = json.loads(response.data)
            return response.data
        else:
            return None

    def concat_data(self, data, start_date, end_date) -> dict:
        parsed_data = []
        for day, price in data["Time Series (Daily)"].items():
            date = datetime(day)
            if date > start_date and date < end_date:
                parsed_data.append({day: price})
            
            if date > end_date:
                break

        return parsed_data

    def intraday_data(self, symbol):
        pass

