import importlib
from django.db import models

# Create your models here.
#TODO : Método para retornar number_of_candles
#TODO : Transformar em modelo do Django (?)

class Trader:

    #INSTANCIAMENTO DAS FERRAMENTAS
    #Contuará assim, porém trocar o importlib por "from ... import"
    def __init__(self, operation_name):
        self.metadata = OperationMetadata(operation_name)

        self.broker = getattr(
            importlib.import_module(
                "brokers.models"),
            self.metadata.broker_id)(self.metadata.market_info)

        self.position_verifier = getattr(
            importlib.import_module(
                "DEPRECATED-positionverifiers.models"),
            self.metadata.position_verifier_id
        )

        self.stop_checker = getattr(
            importlib.import_module(
                "stopcheckers.models"),
            self.stop_checker_id
        )

        self.n_samples = max(
            self.position_verifier.min_samples(),
            self.stop_checker.min_samples()
        )

    def run_real_trade(self):

        data_handler = DataHandler()

        data_handler.real_data = self.broker.get_data(n_samples)

        while True:

            fresh_data = self.broker.get_data(1)

            data = data_handler.refresh_with(fresh_data)

            stop = self.stop_checker(
                data,
                self.metadata.current_position
            )

            #Parei aqui

















            self.metadata.position_memo.update(stop)

            position = self.data.market_tool.check_position(
                self.metadata.position_setter
            )

            trade = bool(position.side != self.metadata.position_memo.side)

            if trade:

                order = self.broker.execute_trade(
                    position,
                self.metadata.position_memo
                )

                if order.was_executed:

                    self.metadata.position_memo.update(position)
                    pass

                #O preço de stop deve fazer parte do stop. Criar os métodos
                #"update stop" e "update position" e retirar a classe "Position"

class DataHandler:
    pass


#AQUI VIRA OBJETO DO DJANGO COM AS CHOICES VINDO DA FUNÇÃO QUE ESCREVI NO JUPYTER
class OperationMetadata:

    def __init__(self):

        self.broker_id = 'BinanceBroker'

        self.market_info = MarketInfo(
            asset='BTCUSDT',
            candle_interval='12h'
        )

        self.position_setter = {
            "id": "cross_simple_ma",
            "setup": {
                "small": "3",
                "big": "100"
            }
        }

        self.stop_criteria = {"stop": "yes"}

        self.current_position = Position()

    def n_samples(self):
        pass


class MarketInfo:

    def __init__(self, asset, candle_interval):

        self.asset = asset
        self.candle_interval = candle_interval


class Position:

    def __init__(self, exposure=0.0, ref_price=0.0):

        self.side = 'closed'
        self._exposure = exposure
        self._ref_price = ref_price

    def update(self, stop):
        pass