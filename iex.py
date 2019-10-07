import requests
import pandas as pd

IEX_TOKEN = ''
IEX_VERSION = ''
IEX_API = ''

class Stock:
    _symbol = ''

    @classmethod
    def _make_url(cls, query):
        query += '&' if '?' in query else '?'
        return 'https://{}.iexapis.com/{}/{}token={}'.format(IEX_API, IEX_VERSION, query, IEX_TOKEN)

    @classmethod
    def _get(cls, query, parse=True):
        # print(cls._make_url(query))
        resp = requests.get(cls._make_url(query))
        if resp.status_code != 200:
            raise Exception('GET {} {} {}'.format(query, resp.status_code, resp.text))
        return resp.json() if parse else resp.text

    def __init__(self, symbol=None, isin=None):
        # todo
        self._symbol = symbol if symbol else self.mapping(isin)

    def chart(self, range):
        # https://sandbox.iexapis.com/stable/stock/AAPL/chart/1m?token=Tpk_xxx
        query = 'stock/{}/chart/{}'.format(self._symbol, range)
        json_text = self._get(query, parse=False)
        df = pd.read_json(json_text, orient='records', convert_dates=True)
        if len(df) == 0:
            raise Exception('Empty data: {} {}'.format(self._make_url(query), json_text))
        df = df.set_index('date')
        return df

def init(token, version='stable', api='sandbox'):
    global IEX_TOKEN, IEX_VERSION, IEX_API
    IEX_TOKEN = token
    IEX_VERSION = version
    IEX_API = api

def stock(symbol=None, isin=None):
    assert IEX_TOKEN != '', 'Call iex.init(token, api="cloud") first'
    return Stock(symbol, isin)

