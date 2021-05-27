import requests
import json
from config import keys

class ConvertExeption(Exception):
    pass


class CryptoConvertor:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertExeption(f'Нельзя конвертировать валюты друг в друга. ({base})')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertExeption(f'Не удалось обратать валюту {quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertExeption(f'Не удалось обратать валюту {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertExeption(f'Не удалось обратать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[base_ticker]
        return total_base

