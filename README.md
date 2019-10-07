

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
      <td>231.48</td>
      <td>234.64</td>
      <td>Sep 30</td>
      <td>221.81</td>
      <td>230.30</td>
      <td>229.26</td>
      <td>228.03</td>
      <td>230.10</td>
      <td>225.40</td>
      <td>26836800</td>
      <td>26634345</td>
    </tr>
    <tr>
      <th>2019-10-01</th>
      <td>0.63</td>
      <td>0.002813</td>
      <td>0.2860</td>
      <td>230.43</td>
      <td>232.22</td>
      <td>Oct 1</td>
      <td>228.40</td>
      <td>231.13</td>
      <td>233.81</td>
      <td>229.73</td>
      <td>226.10</td>
      <td>225.33</td>
      <td>37549879</td>
      <td>36964121</td>
    </tr>
    <tr>
      <th>2019-10-02</th>
      <td>-5.78</td>
      <td>-0.022770</td>
      <td>-2.5135</td>
      <td>228.61</td>
      <td>229.02</td>
      <td>Oct 2</td>
      <td>225.29</td>
      <td>232.71</td>
      <td>224.71</td>
      <td>233.20</td>
      <td>228.66</td>
      <td>232.18</td>
      <td>36373450</td>
      <td>36082815</td>
    </tr>
    <tr>
      <th>2019-10-03</th>
      <td>1.88</td>
      <td>-0.014334</td>
      <td>0.8665</td>
      <td>231.38</td>
      <td>225.03</td>
      <td>Oct 3</td>
      <td>219.88</td>
      <td>219.20</td>
      <td>224.89</td>
      <td>229.04</td>
      <td>215.48</td>
      <td>222.41</td>
      <td>31733834</td>
      <td>30957763</td>
    </tr>
    <tr>
      <th>2019-10-04</th>
      <td>6.21</td>
      <td>0.014214</td>
      <td>2.9104</td>
      <td>236.71</td>
      <td>230.05</td>
      <td>Oct 4</td>
      <td>231.56</td>
      <td>228.99</td>
      <td>234.99</td>
      <td>230.43</td>
      <td>227.37</td>
      <td>229.44</td>
      <td>35793765</td>
      <td>36380802</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
      <th>2019-09-30</th>
      <td>0.00</td>
      <td>0.000000</td>
      <td>0.0000</td>
      <td>232.70</td>
      <td>27406280</td>
    </tr>
    <tr>
      <th>2019-10-01</th>
      <td>0.64</td>
      <td>0.002789</td>
      <td>0.2904</td>
      <td>234.61</td>
      <td>37247422</td>
    </tr>
    <tr>
      <th>2019-10-02</th>
      <td>-5.82</td>
      <td>-0.023449</td>
      <td>-2.6087</td>
      <td>223.08</td>
      <td>36111255</td>
    </tr>
    <tr>
      <th>2019-10-03</th>
      <td>1.90</td>
      <td>-0.014263</td>
      <td>0.8565</td>
      <td>231.56</td>
      <td>31266500</td>
    </tr>
    <tr>
      <th>2019-10-04</th>
      <td>6.28</td>
      <td>0.013826</td>
      <td>2.8464</td>
      <td>228.54</td>
      <td>36016338</td>
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
