from django.db import models

# Create your models here.

class BinanceBroker:
    def __init__(self, market_info):

        self.market_info = market_info

    def get_data(self, n_samples):
        print('get_data received: ', self.market_info, 'n_candles: ', n_samples)