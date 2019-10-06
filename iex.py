import requests
import pandas as pd

IEX_TOKEN = ''
IEX_VERSION = ''
IEX_API = ''

class Stock:
    _symbol = ''

    @classmethod
    def _make_url(cls, query):
        if not query.endswith('?'):
            query = query + '?'
        return 'https://{}.iexapis.com/{}/{}token={}'.format(IEX_API, IEX_VERSION, query, IEX_TOKEN)

    @classmethod
    def _get(cls, query, parse=True):
        # print(cls._make_url(query))
        resp = requests.get(cls._make_url(query))
        if resp.status_code != 200:
            raise Exception('GET {} {} {}'.format(query, resp.status_code, resp.text))
        if parse:
            return resp.json()
        else:
            return resp.text

    def __init__(self, symbol=None, isin=None):
        if symbol:
            self._symbol = symbol
        else:
            self._symbol = self.mapping(isin)


    def chart(self, range):
        # https://sandbox.iexapis.com/stable/stock/AAPL/chart/1m?token=Tpk_xxx
        json_text = self._get('stock/{}/chart/{}'.format(self._symbol, range), parse=False)
        df = pd.read_json(json_text, orient='records', convert_dates=True)
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

