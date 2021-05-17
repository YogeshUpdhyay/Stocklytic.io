import json
import yfinance as yf
import requests_cache
import datetime
import numpy as np

from config import TestConfig as config

class Stock:
    def __init__(self) -> None:
        self.session = requests_cache.CachedSession('yfinance.cache')
        self.session.headers['User-agent'] = 'stockliytic.io/cache'

    def get_data(self, ticker):
        ticker = yf.Ticker(ticker, session=self.session)
        data = ticker.history(period='3mo')
        data.reset_index(inplace=True)
        return data

    def parse_data(self, data, type):

        parsed_data = list()

        if type == "line":
            for index, row in data.iterrows():
                parsed_data.append({str(row['Date']) : {
                    'open': row["Open"],
                    "close": row["Close"],
                    "high": row["High"],
                    "low": row["Low"]
                }})

        return parsed_data
        

