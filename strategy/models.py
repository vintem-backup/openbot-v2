from django.db import models

# Create your models here.
class SideDefiner:

    def __init__(self, side_definer_parameters: dict):
        """

        :type side_definer_parameters: json_dict
        """
        self.side_definer_parameters = side_definer_parameters

    def cros_ma(self, data: dict):

        print("side_definer_parameters: ", self.side_definer_parameters)
        print(" ")
        print("data: ", data)


class StopTest:

    def __init__(self, stop_test_parameters: dict, trading_state: dict):
        """

        :type trading_state: dict
        :type stop_test_parameters: dict
        """

        self.stop_test_parameters = stop_test_parameters
        self.trading_state = trading_state

    class TrendingStopDoubleTrigger:

        def __int__(self, data: dict):
            pass