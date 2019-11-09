from django.db import models

price_composition_options = [
    ("o", "open"),
    ("h", "high"),
    ("l", "low"),
    ("c", "close"),
    ("hl2", "(h + l)/2"),
    ("hlc3", "(h +l + c)/3"),
    ("ohlc4", "(o + h + l + c)/4"),
]

class DefaultCrossSma(models.Model):
    setup_name = models.CharField(
        "Classifier setup name",
        max_length=10,
        primary_key=True
    )

    larger_sampling = models.IntegerField(
        "Number of samples that compose longest average",
        default=100
    )

    smaller_sampling = models.IntegerField(
        "Number of samples that compose smallest average",
        default=3
    )

    price_composition = models.CharField(
        "What value should be considered as price? "
        "Open, close, high, low or a combination of these?",
        max_length=5,
        choices= price_composition_options,
        default='ohlc4'
    )

    def __str__(self):
        return self.setup_name

    def min_samples(self):
        return self.larger_sampling

    def classify(self, data):
        pass
