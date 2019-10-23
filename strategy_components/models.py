# Create your models here.

from django.db import models


class Position:

    def __init__(self):
        self.side = "closed"
        self.exposure = 0.0
        self.ref_price_to_stop_long = 0.0
        self.ref_price_to_stop_short = 0.0


class Exchange(models.Model):
    name = models.CharField(max_length=20)

    api_key = models.CharField(max_length=20)

    api_secret = models.CharField(max_length=20)


class StrategyParameters(models.Model):
    pass


class MetaData(models.Model):

    name = models.CharField(max_length=20)
    position = Position()
    strategy_parameters = models.ForeignKey(StrategyParameters,
                                            on_delete=models.CASCADE)


class Strategy:
    def __init(id)__:
        pass
