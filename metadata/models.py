from django.db import models

# Create your models here.

class TradeMetadata(models.Model):

    trade_metadata_name = models.CharField(max_length=15)

    strategy_metadata_name = models.ForeignKey(
        'StrategyMetadata',
        on_delete=CASCADE,
    )

    exchange = models.ForeignKey(
        'Exchange',
        on_delete=CASCADE,
    )

    asset_symbol = models.CharField(max_length=5)
    # TODO : Implementar choices
    trade_interval = models.CharField(max_length=3)

    candle_interval = models.CharField(max_length=3)

    position = models.ForeignKey('Position', on_delete=)

    def _str__(self):
        return self.trade_metadata_name


class StrategyMetadata(models.Model):

    strategy_name = models.CharField(max_length=15)
    strategy_setup = JSONField()

    def _str__(self):
        return self.strategy_name


class Exchange(models.Model):
    #TODO : guardar api_key e api_secret de forma segura
    name = models.CharField(max_length=15)

    apy_key = models.CharField(max_length=30)

    apy_secret = models.CharField(max_length=30)

    def __str__(self):
        return self.name







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