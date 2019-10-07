import requests
import pandas as pd
from urllib.parse import urlencode

IEX_TOKEN = ''
IEX_VERSION = ''
IEX_API = ''

class Stock:
    _symbol = ''

    @classmethod
    def _make_url(cls, paths, params):
        query = '/'.join(paths)
        params['token'] = IEX_TOKEN
        query += '?' + urlencode(params)
        return 'https://{}.iexapis.com/{}/{}'.format(IEX_API, IEX_VERSION, query)

    @classmethod
    def _get(cls, paths, params, parse=False):
        url = cls._make_url(paths, params)
        resp = requests.get(url)
        if resp.status_code != 200:
            raise Exception('GET {} {} {}'.format(url, resp.status_code, resp.text))
        return resp.json() if parse else resp.text

    def __init__(self, symbol=None, isin=None):
        # todo
        self._symbol = symbol if symbol else self.mapping(isin)

    def _records(self, paths, params, date_col):
        json_text = self._get(paths, params)
        df = pd.read_json(json_text, orient='records', convert_dates=True)
        if len(df) == 0:
            raise Exception('Empty data: {} {}'.format(self._make_url(paths, params), json_text))
        df = df.set_index(date_col)
        return df

    def chart(self, range, **params):
        # https://sandbox.iexapis.com/stable/stock/AAPL/chart/1m?token=Tpk_xxx
        paths = ['stock', self._symbol, 'chart', range]
        return self._records(paths, params, 'date')

    def splits(self, range, **params):
        paths = ['stock', self._symbol, 'splits', range]
        return self._records(paths, params, 'exDate')

    def dividends(self, range, **params):
        paths = ['stock', self._symbol, 'dividends', range]
        return self._records(paths, params, 'exDate')

    def news(self, last, **params):
        paths = ['stock', self._symbol, 'news/last', str(last)]
        return self._records(paths, params, 'datetime')

def init(token, version='stable', api='sandbox'):
    global IEX_TOKEN, IEX_VERSION, IEX_API
    IEX_TOKEN = token
    IEX_VERSION = version
    IEX_API = api

def stock(symbol=None, isin=None):
    assert IEX_TOKEN != '', 'Call iex.init(token, api="cloud") first'
    return Stock(symbol, isin)

