

```python
%load_ext autoreload
%autoreload 2
```

# Simple IEX Stock Fetcher

The IEX free message quota only gets one year of data for 200 stocks, so run this, fetcher stock data and save to disk every month.


## Test api


```python
import iex
import key
iex.init(key.test_token, api='sandbox')
aapl = iex.Stock('AAPL')
aapl.chart('5d')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>change</th>
      <th>changeOverTime</th>
      <th>changePercent</th>
      <th>close</th>
      <th>high</th>
      <th>label</th>
      <th>low</th>
      <th>open</th>
      <th>uClose</th>
      <th>uHigh</th>
      <th>uLow</th>
      <th>uOpen</th>
      <th>uVolume</th>
      <th>volume</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2019-09-30</th>
      <td>0.00</td>
      <td>0.000000</td>
      <td>0.0000</td>
      <td>230.20</td>
      <td>230.09</td>
      <td>Sep 30</td>
      <td>229.47</td>
      <td>226.80</td>
      <td>228.40</td>
      <td>227.92</td>
      <td>228.85</td>
      <td>229.90</td>
      <td>26841490</td>
      <td>27506584</td>
    </tr>
    <tr>
      <th>2019-10-01</th>
      <td>0.62</td>
      <td>0.002852</td>
      <td>0.2858</td>
      <td>234.56</td>
      <td>228.73</td>
      <td>Oct 1</td>
      <td>234.70</td>
      <td>226.03</td>
      <td>226.30</td>
      <td>237.90</td>
      <td>230.50</td>
      <td>235.12</td>
      <td>37691578</td>
      <td>37906031</td>
    </tr>
    <tr>
      <th>2019-10-02</th>
      <td>-5.68</td>
      <td>-0.022798</td>
      <td>-2.6024</td>
      <td>219.46</td>
      <td>229.68</td>
      <td>Oct 2</td>
      <td>227.08</td>
      <td>223.94</td>
      <td>219.07</td>
      <td>234.70</td>
      <td>223.84</td>
      <td>234.00</td>
      <td>36483928</td>
      <td>36859828</td>
    </tr>
    <tr>
      <th>2019-10-03</th>
      <td>1.87</td>
      <td>-0.014374</td>
      <td>0.8615</td>
      <td>221.36</td>
      <td>228.88</td>
      <td>Oct 3</td>
      <td>224.74</td>
      <td>226.18</td>
      <td>230.40</td>
      <td>230.14</td>
      <td>217.64</td>
      <td>228.59</td>
      <td>31658842</td>
      <td>30946087</td>
    </tr>
    <tr>
      <th>2019-10-04</th>
      <td>6.26</td>
      <td>0.013779</td>
      <td>2.8933</td>
      <td>236.36</td>
      <td>234.80</td>
      <td>Oct 4</td>
      <td>225.47</td>
      <td>233.62</td>
      <td>229.12</td>
      <td>230.83</td>
      <td>227.00</td>
      <td>229.15</td>
      <td>35594415</td>
      <td>35560415</td>
    </tr>
  </tbody>
</table>
</div>



## Fetcher SPY stocks


```python
import pandas as pd
spy = [x for x in pd.read_html('https://etfdailynews.com/etf/spy/', attrs={'id': 'etfs-that-own'})[0].Symbol.values.tolist() if isinstance(x, str)]
correction = {'PCLN':'BKNG', 'DWDP':'DD'}
```


```python
import os, sys
chart_range = [(5,'break'), (10,'1m'), (45,'3m'), (90,'6m'), (250,'1y'), (99999,'max')]
```


```python
# iex.init(key.test_token, api='sandbox')
iex.init(key.token, api='cloud')

# save historical price to disk
for k in spy:
    if k in correction:
        k = correction[k]
    sys.stdout.write('\r{}   '.format(k))
    filename = "./daily/{}.csv".format(k)
    if os.path.exists(filename):
        # fetcher missing period
        df = pd.read_csv(filename, index_col='date', parse_dates=True)
        td = pd.Timedelta(df.index[-1] - pd.datetime.now())
        for day, param in chart_range:
            if td.days < day:
                if param != 'break':
                    df_append = iex.Stock(k).chart(param)
                    pd.concat([df, df_append]).to_csv(filename)
                break
    else:
        iex.Stock(k).chart('max').to_csv(filename)


```


```python

```
