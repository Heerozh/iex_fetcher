

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
aapl.chart('5d', chartCloseOnly=True)
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
      <th>volume</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2019-10-01</th>
      <td>0.630000</td>
      <td>0.002846</td>
      <td>0.2776</td>
      <td>235.08</td>
      <td>36626895</td>
    </tr>
    <tr>
      <th>2019-10-02</th>
      <td>-5.740000</td>
      <td>-0.023081</td>
      <td>-2.5109</td>
      <td>222.51</td>
      <td>35941685</td>
    </tr>
    <tr>
      <th>2019-10-03</th>
      <td>1.940000</td>
      <td>-0.014185</td>
      <td>0.8914</td>
      <td>231.78</td>
      <td>30438546</td>
    </tr>
    <tr>
      <th>2019-10-04</th>
      <td>6.310000</td>
      <td>0.013995</td>
      <td>2.8347</td>
      <td>230.24</td>
      <td>34995248</td>
    </tr>
    <tr>
      <th>2019-10-07</th>
      <td>0.051249</td>
      <td>0.000000</td>
      <td>0.0200</td>
      <td>234.46</td>
      <td>32130948</td>
    </tr>
  </tbody>
</table>
</div>




```python
aapl.dividends('1y')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>amount</th>
      <th>currency</th>
      <th>date</th>
      <th>declaredDate</th>
      <th>description</th>
      <th>flag</th>
      <th>frequency</th>
      <th>paymentDate</th>
      <th>recordDate</th>
    </tr>
    <tr>
      <th>exDate</th>
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
      <th>2018-11-14</th>
      <td>0.74</td>
      <td>USD</td>
      <td>2019-10-08</td>
      <td>2018-11-10</td>
      <td>er eD lrpfpl$esAa7reP a udDiv. h3 areSeeydicr ...</td>
      <td>QhneQoNCao g</td>
      <td>reayurltQ</td>
      <td>2018-11-29</td>
      <td>2018-11-14</td>
    </tr>
  </tbody>
</table>
</div>



## Fetcher SPY stocks


```python
import pandas as pd
spy = [x for x in pd.read_html('https://etfdailynews.com/etf/spy/', attrs={'id': 'etfs-that-own'})[0].Symbol.values.tolist()
       if isinstance(x, str)]
correction = {'PCLN':'BKNG', 'DWDP':'DD'}
```


```python
import os, sys
chart_range = [(5,'5d'), (20,'1m'), (75,'3m'), (165,'6m'), (341,'1y'), (715,'2y'), (99999,'max')]
```


```python
# iex.init(key.test_token, api='sandbox')
iex.init(key.token, api='cloud')

# save historical price to disk
for k in spy:
    k = correction[k] if k in correction else k
    sys.stdout.write('\r{}   '.format(k))
    filename = "./daily/{}.csv".format(k)
    if os.path.exists(filename):
        # fetcher missing period
        df = pd.read_csv(filename, index_col='date', parse_dates=True)
        days = pd.Timedelta(df.index[-1] - pd.datetime.now()).days
        bdays = len(pandas.bdate_range(df.index[-1], pd.datetime.now())) - 1
        for day, param in chart_range:
            if bdays <= 0:
                break
            elif days < day:
                df_append = iex.Stock(k).chart(param)
                pd.concat([df, df_append]).to_csv(filename)
                break
    else:
        iex.Stock(k).chart('max').to_csv(filename)


```


```python

```


```python

```
