from metaapi_cloud_sdk import MetaApi as MetaApiCalls
import time
import warnings
from datetime import datetime as dt, timezone

import alpaca_trade_api
import pandas as pd
from alpaca_trade_api.rest import APIError as AlpacaAPIError, TimeFrame

from blankly.exchanges.interfaces.exchange_interface import ExchangeInterface
from blankly.exchanges.orders.limit_order import LimitOrder
from blankly.exchanges.orders.market_order import MarketOrder
from blankly.exchanges.orders.stop_loss import StopLossOrder
from blankly.exchanges.orders.take_profit import TakeProfitOrder
from blankly.utils import utils as utils
from blankly.utils.exceptions import APIException
from blankly.utils.time_builder import build_minute, time_interval_to_seconds, number_interval_to_string
import asyncio
class MetaApiInterface(ExchangeInterface):
    def __init__(self, exchange_name, authenticated_api):
        self.__unique_assets = None
        self.account_id = '5b5582fc-87b0-4f43-a437-79bd1b4cd706'
        super().__init__(exchange_name, authenticated_api, valid_resolutions=[60, 60 * 5, 60 * 15,
                                                                              60 * 60 * 24])
        assert isinstance(self.calls, MetaApiCalls)

    def init_exchange(self):
        pass

    async def get_products(self) -> dict:
        assets = {}
        return assets
    
    @property
    def cash(self):
        account_dict = self.calls.get_account()
        return float(account_dict['buying_power'])

    @utils.enforce_base_asset
    async def get_account(self, symbol=None):
        """
        Get all assets in an account, or sort by symbol/account_id
        Args:
            symbol (Optional): Filter by particular symbol

            These arguments are mutually exclusive

        """
        symbol = super().get_account(symbol=symbol)

        needed = self.needed['get_account']
        parsed_dictionary = utils.AttributeDict({})
        
        
        
        if symbol is not None:

    @utils.order_protection
    def market_order(self, symbol, side, size) -> MarketOrder:
        assert isinstance(self.calls, alpaca_trade_api.REST)

        needed = self.needed['market_order']
        order = utils.build_order_info(0, side, size, symbol, 'market')

        # TODO: MetaApi market order

        response = self._fix_response(needed, response)
        return MarketOrder(order, response, self)

    @utils.order_protection
    def limit_order(self, symbol: str, side: str, price: float, size: float) -> LimitOrder:
        needed = self.needed['limit_order']
        order = utils.build_order_info(price, side, size, symbol, 'limit')

        # TODO: MetaApi limit order

        response = self._fix_response(needed, response)
        return LimitOrder(order, response, self)

    @utils.order_protection
    def take_profit_order(self, symbol: str, price: float, size: float) -> TakeProfitOrder:
        side = 'sell'
        needed = self.needed['take_profit']
        order = utils.build_order_info(price, side, size, symbol, 'take_profit')

        # TODO: MetaApi take profit order

        response = self._fix_response(needed, response)
        return TakeProfitOrder(order, response, self)

    @utils.order_protection
    def stop_loss_order(self, symbol: str, price: float, size: float) -> StopLossOrder:
        side = 'sell'
        needed = self.needed['stop_loss']
        order = utils.build_order_info(price, side, size, symbol, 'stop_loss')

        # TODO: MetaApi stop loss order

        response = self._fix_response(needed, response)
        return StopLossOrder(order, response, self)

    def _fix_response(self, needed, response):
        response = self.__parse_iso(response)
        response = utils.rename_to([
            ['limit_price', 'price'],
            ['qty', 'size']
        ], response)
        response = utils.isolate_specific(needed, response)
        if 'time_in_force' in response:
            response['time_in_force'] = response['time_in_force'].upper()
        return response

    def cancel_order(self, symbol, order_id) -> dict:
        assert isinstance(self.calls, alpaca_trade_api.REST)
        self.calls.cancel_order(order_id)

        # TODO: handle the different response codes
        return {'order_id': order_id}

    def get_open_orders(self, symbol=None):
        assert isinstance(self.calls, alpaca_trade_api.REST)
        # TODO: write this function

    def get_order(self, symbol, order_id) -> dict:
        assert isinstance(self.calls, alpaca_trade_api.REST)
        # TODO: write this function

    def get_fees(self, symbol):
        assert isinstance(self.calls, alpaca_trade_api.REST)
        # TODO: write this function

    async def get_product_history(self, symbol: str, epoch_start: float, epoch_stop: float, resolution: int):
        assert isinstance(self.calls, MetaApiCalls)
        account = await self.calls.metatrader_account_api.get_account(self.account_id)
        bars = await account.get_historical_candles(symbol = symbol, start_time = epoch_stop_str)
        # TODO: write this function

    def get_order_filter(self, symbol: str):
        assert isinstance(self.calls, alpaca_trade_api.REST)
        # TODO: write this function

    def get_price(self, symbol) -> float:
        assert isinstance(self.calls, alpaca_trade_api.REST)
        # TODO: write this function