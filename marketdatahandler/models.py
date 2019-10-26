# TODO : Refatorar os atributos para _atributos e criar os métodos setter para os mesmos

import pandas as pd
from django.db import models

# Create your models here.
class MarketDataContainer:

    def __init__(self) -> None:
        self.raw_data = pd.DataFrame()

    def transform_to_candle(self, candle_interval: str) -> pd.DataFrame:
        pass

    def return_price(self, source: str = 'olh4') -> object:
        pass


class RealMarketData(MarketDataContainer):

    def __init__(self, parameters) -> None:
        
        super().__init__()
        self._parameters = parameters
        self._to_analyze = pd.DataFrame()

     def __str__(self) -> str:
        return '< Instance of {} at address:{}>'.format(self.__class__.__name__, id(self))

    @property
    def parameters(self):
        return self._parameters

    @property
    def to_analyze(self) -> pd.DataFrame:
        return self._to_analyze

    @to_analyze.setter
    def to_analyze(self, data_to_analyze: pd.DataFrame) -> None:
        """

        :type data_to_analyze: Pandas Dataframe
        """
        self._to_analyze = data_to_analyze

    def create(self):

        self.raw_data = (pd.read_csv(
            'marketdatahandler/test-data.csv')
        ).drop(['Unnamed: 0'], axis=1)

    def refresh(self):
        pass


class TestMarketData(MarketDataContainer):

    def __init__(self, parameters):

        self.parameters = parameters
        self.raw_data = pd.DataFrame()
        self.to_analyze = pd.DataFrame()
        self.refresh_query_counter = 0
        self.is_refreshable = True

    def create(self):
        pass

    def refresh(self):
        pass