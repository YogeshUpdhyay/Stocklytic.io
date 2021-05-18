import json
import yfinance as yf
import requests_cache
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

    def parse_data(self, data):

        parsed_data = list()
        indicator = False

        if "Indicator" in data.columns:
            indicator = True

        data = data.dropna(axis=0)

        for index, row in data.iterrows():
            temp = {
                'date': str(row['Date']),
                'open': row["Open"],
                "close": row["Close"],
                "high": row["High"],
                "low": row["Low"]
            }

            if indicator:
                temp["indicator"] = row['Indicator']

            parsed_data.append(temp)

        return parsed_data
        

