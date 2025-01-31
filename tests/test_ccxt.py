# Project Modules

from pkg_quanty.data.providers.ccxt_api import ProviderCCXT, ExchangeNames, TokenPairs
from pkg_quanty.data.providers.utils import get_timestamp_8601

# Other Modules

from dotenv import load_dotenv
import os

# Initial Parameters

load_dotenv("global_vars.env")
api_key = os.getenv("BINANCE_API_KEY")
secret_key = os.getenv("BINANCE_SECRET_KEY")
exchange_name = ExchangeNames.binance
pair = TokenPairs.eth_usdt
date = get_timestamp_8601(year=2024, month=11, day=5,
                          hour=3, minutes=0, seconds=0, tz_sign="+", tz_hour=0)

api = ProviderCCXT(exchange_name=exchange_name,
                   api_key=api_key, api_secret=secret_key)

# Test Functions


def test_connect(capsys):

    api.connect()

    captured = capsys.readouterr()

    if exchange_name == ExchangeNames.binance:
        assert captured.out.strip() == "Connected to Binance API."


def test_get_market_data(capsys):

    _ = api.get_market_data(symbol=pair)
    captured = capsys.readouterr()

    assert captured.out.strip() == "Market data fetched."


def test_get_order_book(capsys):

    _ = api.get_order_book(symbol=pair, depth=20)
    captured = capsys.readouterr()

    assert captured.out.strip() == "Order book data fetched."


def test_get_transactions(capsys):

    _ = api.get_transactions(symbol=pair, since=date)
    captured = capsys.readouterr()

    assert captured.out.strip() == "Trade data fetched."
