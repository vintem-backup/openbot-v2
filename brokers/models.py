from django.db import models

# Create your models here.
class BrokersList(models.Model):
    name = models.CharField(
        "Exchange name",
        max_length=10,
        primary_key=True,
    )

    #TODO: Capturar essas informações de maneira segura
    api_key = models.CharField(
        "Api Key",
        max_length=20,
        blank=True,
        null=True
    )
    api_secret = models.CharField(
        "Api Secret",
        max_length=20,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

#Provisoria pra criar o market_info
class MarketInfo(models.Model):
    asset = models.CharField(max_length=10)
    candle_interval = models.CharField(max_length=3)


class BinanceBroker(models.Model):
    broker_info = models.ForeignKey(
        BrokersList,
        on_delete=models.PROTECT
    )
    market_info = models.ForeignKey(
        MarketInfo,
        on_delete=models.CASCADE
    )


    def get_data(self, n_samples):

        print(n_samples)
