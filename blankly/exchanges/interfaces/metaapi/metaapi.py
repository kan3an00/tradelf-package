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
        options = {}
        MetaApiCalls.enable_logging()
        loop = asyncio.new_event_loop()
        calls = MetaApiCalls(token=auth["API_KEY"], opts=options)
        try:
            account = loop.create_task(calls.metatrader_account_api.get_account('5b5582fc-87b0-4f43-a437-79bd1b4cd706'))
        except Exception as e:
            raise LookupError("MetaApi API call failed")
        try:
            if account.state != 'DEPLOYED':
                warnings.warn('Your MetaApi account is indicated as blocked for trading....')
        except KeyError:
            raise LookupError("alpaca API call failed")
        connection = account.get_streaming_connection()
        loop.create_task(connection.connect())
        loop.create_task(connection.wait_synchronized({'timeoutInSeconds': 600}))
        loop.run_until_complete()
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
