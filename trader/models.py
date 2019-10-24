# Create your models here.
#from django.db import models

import importlib
import time

from components.models import MetaData
from marketdatahandler.models import RealMarketData
from orderhandler.models import RealOrders

# TODO : Atenção para os métodos privados

'''ORGANIZAÇÃO DOS DADOS
    
    - metadata      -- Parâmetros de controle e acompanhamento do trade, como:
                        
                        - id do metadata
                        - id do setup de estratégia
                        - dados da corretora (usuário, senha)
                        - identificação do mercado (nome da corretora e ativo)
                        - trade_interval
                        - candle_interval
                        - posição:
                            * lado
                            * tamanho
                            * ref_stop_price
'''

class Trader:

    def __init__(self, metadata_name: str):

        # TODO : Metadata como model do django
        self.metadata = MetaData(id=metadata_name)

        Strategy = getattr(importlib.import_module("components.models"),
                           self.metadata.strategy_name)

        # TODO : Strategy como model do django
        self.strategy = Strategy(id=self.metadata.strategy_setup)

    def run_for_real(self):
        '''Todos os passos do trade, como verificar stop, definir posição, disparar ordem
        corretamente para corretora correspondente, etc. Repetir indefinidamente

        :return: trader -- A celery object which defines the state of trading_run loop function.
        '''

        # TODO : verificar se o trader está ativo para o mesmo trade. Emitir alerta caso esteja.

        self.data_handler = RealMarketData(self.metadata)

        self.order = RealOrders(self.metadata.exchange)

        trader = self.trading_run(self)

        return trader

    # @celery
    def trading_run(self):

        while True:

            # TODO escrever corretamente método/prorpiedade
            self.strategy.data_to_analyze = self.data_handler.refresh_data()

            signal = self.strategy.chek_for_signal(self.metadata.position)

            if signal.is_trade:

                trade = self.order.execute(signal.trade)

                if trade.is_done:

                    # TODO escrever corretamente método/prorpiedade
                    self.metadata.position.side = signal.trade["new_side"]
                    # TODO : Appendar no trade_history

            #TODO : função do timesleep
            time.sleep(self.sleep_time)

    # @celery
    def run_in_back_testing(self,
                            from_sample="Oldest",
                            trade_history='Append',
                            continuous_mode=True):
        '''Todos os passos do trade, como verificar stop, definir posição, disparar ordem
        simulada, appendar o histórico de trade em banco de dados próprio, etc.


        :keyword from_sample(str)   -- Timestamp of the market data sample that will starts
                                       the simulation. E.g.: '2019-10-15 13:04:00'
                                       Default="Oldest", takes the oldest data available.

        :keyword trade_history(str) -- 'Append' or 'Replace' if matching table is found.

        :keyword

        '''

        pass