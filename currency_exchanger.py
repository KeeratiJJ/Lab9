import requests
from datetime import datetime
from unittest.mock import Mock


class CurrencyExchanger:
    def __init__(self, base_currency="THB", target_currency="USD"):
        self.currency_api = "https://coc-kku-bank.com/foreign-exchange"
        self.base_currency = base_currency
        self.target_currency = target_currency
        self.ex_date = datetime.today().date()
        self.api_response = None

    def get_currency_rate(self):
        try:
            # Get the exchange rate
            p = {'from': self.base_currency, 'to': self.target_currency}
            response = requests.get(self.currency_api, params=p)
            if response.status_code in (200, 201):
                self.api_response = response.json()
        except requests.exceptions.RequestException:
            self.api_response = None

    def currency_exchange(self, amount):
        self.get_currency_rate()
        if self.api_response and 'result' in self.api_response:
            # Get the exchange rate from the API response
            exchange_rate = self.api_response['result'].get(self.target_currency)
            if exchange_rate:
                # Calculate the converted amount
                converted_amount = amount * exchange_rate
                return converted_amount
        return None