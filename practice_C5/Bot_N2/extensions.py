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
            two_currency = f'{quote_ticker}_{base_ticker}'
        except KeyError:
            raise ConvertExeption(f'Не удалось обратать валюту {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertExeption(f'Не удалось обратать количество {amount}')

        r = requests.get(f'https://free.currconv.com/api/v7/convert?q={quote_ticker}_{base_ticker}&compact=ultra&apiKey=62a2f91e719ec3ac6d67')
        total_base = json.loads(r.content)[two_currency]
        return total_base*amount

