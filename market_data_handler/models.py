from django.db import models

# Create your models here.

class GetFromExchange:
    pass


class PriceSerie:

    def __init__(self, price_source: str):

        self.source = price_source

    def calculate(self, market_data: dict):

        olh4 = bool(self.source == 'olh4')

        if olh4:
            price = (1/4)*(market_data['open'] +
                     market_data['high'] +
                     market_data['low'] +
                     market_data['close'])

        else:
            price = market_data[self.source]

        return price


class TransformCandle:

    def __init__ (self, candle_dict: dict):
        self.candle_dict = candle_dict

    def from_1m_to(self, out_format: str):
        pass


class SaveInDb:
    pass


class ReadFromDb:
    pass


class Integrity:

    def __init__(self):
        pass

    def test(self):
        pass

    def adjust(self):
        pass