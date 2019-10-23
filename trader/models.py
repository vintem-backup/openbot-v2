# Create your models here.
#from django.db import models

import importlib
import time
#from trade_parameters import Metadata
from strategy_components.models import MetaData, Strategy
from market_data_handler.models import RealMarketData, BacktestMarketData
from order_handler.models import BacktestOrder

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

        self.metadata = MetaData(id=metadata_name)
        self.strategy = Strategy(id=self.metadata.strategy_id)

    def run(self, mode):
        """

        :type mode: list
        """
        real_trade = 'rt' in mode
        backtesting = 'bt' in mode
        both = bool(real_trade and backtesting)

        if real_trade:
            # Corre em celery run_for_real
            pass

        if backtesting:
            # Corre em celery run_in_back_testing
            pass

        if both:
            # Corre cada um em um celery diferente
            pass

    # @celery
    def run_for_real(self):
        '''Todos os passos do trade, como verificar stop, definir posição, disparar ordem
        corretamente para corretora correspondente, etc. Repetir indefinidamente

        :return:
        '''

        data_handler = RealMarketData(self.metadata)

        order_performer = getattr(importlib.import_module("order_handler.models"),
                                  self.metadata.exchange)

        while True:

            self.strategy.data_to_analyze = data_handler.refresh_data()

            long = bool(self.metadata.position.side == 'long')
            short = bool(self.metadata.position.side == 'short')

            if long:

                stop_long = self.strategy.is_stop_long(self.metadata.position)

                if stop_long:

                    stop_order = order_performer.do_stop_long(self.metadata)

                    is_done = order_performer.check_order(stop_order)

                    if is_done:

                        self.metadata.position.side = 'closed'
                        # TODO : Appendar no trade_history
                else:

                    self.strategy.review_stop_price(self.metadata.position)

            if short:
                # TODO : testar stop para a posição venda (a descoberto)
                pass

            new_side = self.strategy.define_side()

            trade_signal = bool(new_side != self.metadata.position.side)

            if trade_signal:

                trade_order = order_performer.do_trade(self.metadata)

                is_done = order_performer.check_order(trade_order)

                if is_done:

                    self.metadata.position.side = new_side
                    # TODO : Appendar no trade_history

            #strategy.update_ref_prices

            #TODO : função do timesleep
            time.sleep(self.strategy.calcule_sleep_for((self.metadata.trade_interval)))

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