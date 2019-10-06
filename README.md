```python
%load_ext autoreload
%autoreload 2
```

# IEX Stock Fetcher

The IEX free message quota only gets one year of data for 200 stocks, so run this, fetcher stock data and save to disk every month.


## Test api


```python
import iex
iex.init('Tpk_8dad7c6b1806466dbb3c1b3c07fa5be1', api='sandbox')
aapl = iex.Stock('AAPL')
aapl.chart('5d')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
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
      <td>233.55</td>
      <td>232.94</td>
      <td>Sep 30</td>
      <td>221.48</td>
      <td>224.00</td>
      <td>228.49</td>
      <td>226.79</td>
      <td>229.87</td>
      <td>221.00</td>
      <td>26324314</td>
      <td>26990686</td>
    </tr>
    <tr>
      <th>2019-10-01</th>
      <td>0.64</td>
      <td>0.002867</td>
      <td>0.2789</td>
      <td>231.94</td>
      <td>236.72</td>
      <td>Oct 1</td>
      <td>231.30</td>
      <td>226.46</td>
      <td>226.77</td>
      <td>237.37</td>
      <td>232.20</td>
      <td>228.45</td>
      <td>37300050</td>
      <td>37740641</td>
    </tr>
    <tr>
      <th>2019-10-02</th>
      <td>-5.70</td>
      <td>-0.022807</td>
      <td>-2.6285</td>
      <td>223.67</td>
      <td>231.00</td>
      <td>Oct 2</td>
      <td>226.87</td>
      <td>223.61</td>
      <td>219.79</td>
      <td>233.90</td>
      <td>222.10</td>
      <td>233.27</td>
      <td>37190954</td>
      <td>36897959</td>
    </tr>
    <tr>
      <th>2019-10-03</th>
      <td>1.95</td>
      <td>-0.014448</td>
      <td>0.8510</td>
      <td>229.09</td>
      <td>224.64</td>
      <td>Oct 3</td>
      <td>223.64</td>
      <td>222.83</td>
      <td>228.46</td>
      <td>224.76</td>
      <td>222.09</td>
      <td>220.24</td>
      <td>31829034</td>
      <td>31639591</td>
    </tr>
    <tr>
      <th>2019-10-04</th>
      <td>6.22</td>
      <td>0.014130</td>
      <td>2.8757</td>
      <td>230.11</td>
      <td>232.69</td>
      <td>Oct 4</td>
      <td>229.78</td>
      <td>235.12</td>
      <td>236.55</td>
      <td>227.84</td>
      <td>228.39</td>
      <td>231.80</td>
      <td>36212147</td>
      <td>35343376</td>
    </tr>
  </tbody>
</table>
</div>



## Fetche SPY stocks


```python
import pandas as pd
spy = [x for x in pd.read_html('https://etfdailynews.com/etf/spy/', attrs={'id': 'etfs-that-own'})[0].Symbol.values.tolist() if isinstance(x, str)]
```


```python
# iex.init('pk_xxx', api='cloud')
iex.init('Tpk_8dad7c6b1806466dbb3c1b3c07fa5be1', api='sandbox')
for k in spy:
    # todo read csv and add needed range
    iex.Stock(k).chart('1y').to_csv("./daily/{}.csv".format(k))
```


```python

```


```python
 
```


```python

```


```python

```


```python

```


```python

```
