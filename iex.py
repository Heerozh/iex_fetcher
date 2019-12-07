import requests
import pandas as pd
from urllib.parse import urlencode

IEX_TOKEN = ''
IEX_VERSION = ''
IEX_API = ''


class IEX_API:
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

    @classmethod
    def _records(cls, paths, params, date_col):
        """ Convert json to record orient df, and index as date_col """
        json_text = cls._get(paths, params)
        df = pd.read_json(json_text, orient='records')
        if len(df) == 0:
            raise EOFError('Empty data: {} {}'.format(cls._make_url(paths, params), json_text))
        df = df.set_index(date_col)
        df.index = pd.to_datetime(df.index)
        return df

    @classmethod
    def _json(cls, paths, params):
        return cls._get(paths, params, parse=True)

#----------------------------------------------------------------

class Reference(IEX_API):

    @classmethod
    def symbols(cls, **params):
        paths = ['ref-data', 'symbols']
        return cls._records(paths, params, 'date')

#----------------------------------------------------------------

class Stock(IEX_API):
    _symbol = ''

    def __init__(self, symbol=None, isin=None):
        # todo
        self._symbol = symbol if symbol else self.mapping(isin)

    def company(self, **params):
        paths = ['stock', self._symbol, 'company']
        return self._json(paths, params)

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

#----------------------------------------------------------------

def init(token, version='stable', api='sandbox'):
    global IEX_TOKEN, IEX_VERSION, IEX_API
    IEX_TOKEN = token
    IEX_VERSION = version
    IEX_API = api

def stock(symbol=None, isin=None):
    assert IEX_TOKEN != '', 'Call iex.init(token, api="cloud") first'
    return Stock(symbol, isin)

