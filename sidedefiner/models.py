from django.db import models

# Create your models here.

class Default:

    def __init__(self, args):

        self.args = args

    def test_method(self):

        print(self.args)
