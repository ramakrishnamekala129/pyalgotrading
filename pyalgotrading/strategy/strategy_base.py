from abc import ABCMeta, abstractmethod
from collections import defaultdict

import broker


class StrategyBase(object, metaclass=ABCMeta):
    """
    Dummy placeholder class. Here to ensure all required methods are implemented and as per requirements.

    Once uploaded, this strategy will be replaced with the real base class strategy
    """

    def __init__(self, *args, **kwargs):
        # Dummy attributes
        self.strategy_parameters = defaultdict(lambda: 'dummy')
        self.strategy_mode = StrategyMode.INTRADAY  # <Type: Enum of type StrategyMode; This attribute will hold one of the following values - StrategyMode.INTRADAY or StrategyMode.DELIVERY. This value is passed to pyalgotrading.algobulls.connection.backtest/papertest/realtrade methods.>
        self.number_of_lots = 1  # <Type: This attribute will hold one of the following values - StrategyMode.INTRADAY or StrategyMode.DELIVERY. This value is passed to pyalgotrading.algobulls.connection.backtest/papertest/realtrade methods.>
        self.broker = broker.broker_connection_base.BrokerConnectionBase()
        self.utils = broker.utils
        self.BuyOrderRegular = BuyOrderRegular
        self.SellOrderRegular = SellOrderRegular
        self.BuyOrderBracket = BuyOrderBracket
        self.SellOrderBracket = SellOrderBracket

    @staticmethod
    @abstractmethod
    def name():
        raise NotImplementedError

    def get_historical_data(self, instrument):
        pass

    @staticmethod
    @abstractmethod
    def versions_supported():
        """
        :return: Should return a single version or list of versions of ABC on which the current strategy has been tested to run successfully
        """
        raise NotImplementedError

    @abstractmethod
    def initialize(self):
        """
        Initialization task for this strategy. Calling this method should initialise/reset the strategy's internal state variables to original state.

        Every Strategy should initialize its internal state variables in this task to reset values.

        Indented to be called by TLS as part of pre market activity & for backtesting mode, at the start of every new backtesting day.
        """
        raise NotImplementedError

    def strategy_select_instruments_for_entry(self, candle, instruments_bucket):
        raise NotImplementedError

    @abstractmethod
    def strategy_enter_position(self, candle, instrument, sideband_info):
        raise NotImplementedError

    @abstractmethod
    def strategy_select_instruments_for_exit(self, candle, instruments_bucket):
        raise NotImplementedError

    @abstractmethod
    def strategy_exit_position(self, candle, instrument, sideband_info):
        raise NotImplementedError