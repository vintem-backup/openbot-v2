from django.db import models

# Create your models here.
class Trader:

    def __init__(self, trade_parameters: dict):

        self.trade_parameters = trade_parameters

    def run_for_real(self):
        '''Todos os passos do trade, como verificar stop, definir posição, disparar ordem
        corretamente para corretora correspondente, etc. Repetir indefinidamente

        :return:
        '''

        pass

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