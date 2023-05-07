from metaapi_cloud_sdk import MetaApi as MetaApiCalls

from blankly.exchanges.exchange import Exchange
from blankly.exchanges.auth.utils import load_auth
import asyncio
import warnings

class MetaApi(Exchange):
    def __init__(self, portfolio_name=None, keys_path="keys.json", settings_path=None):
        Exchange.__init__(self, "metaapi", portfolio_name, settings_path)

        # Load the auth from the keys file
        auth = load_auth("metaapi", keys_path)
        MetaApiCalls.enable_logging()
        calls = MetaApiCalls(token=auth["API_KEY"])
        
        # Always finish the method with this function
        super().construct_interface_and_cache(calls)

    def get_exchange_state(self):
        return self.interface.get_products()

    def get_asset_state(self, symbol):
        return self.interface.get_account(symbol)

    def get_direct_calls(self):
        return self.calls

    def get_market_clock(self):
        return self.calls.get_clock()
