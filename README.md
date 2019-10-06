```python
%load_ext autoreload
%autoreload 2
```

# IEX Stock Fetcher

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
      <td>232.57</td>
      <td>233.01</td>
      <td>Sep 30</td>
      <td>230.73</td>
      <td>222.40</td>
      <td>228.30</td>
      <td>229.41</td>
      <td>221.60</td>
      <td>227.30</td>
      <td>27560717</td>
      <td>27356318</td>
    </tr>
    <tr>
      <th>2019-10-01</th>
      <td>0.64</td>
      <td>0.002815</td>
      <td>0.2826</td>
      <td>226.01</td>
      <td>233.05</td>
      <td>Oct 1</td>
      <td>229.60</td>
      <td>232.19</td>
      <td>232.83</td>
      <td>237.84</td>
      <td>228.60</td>
      <td>230.65</td>
      <td>37151742</td>
      <td>37308230</td>
    </tr>
    <tr>
      <th>2019-10-02</th>
      <td>-5.75</td>
      <td>-0.022611</td>
      <td>-2.5684</td>
      <td>227.78</td>
      <td>229.09</td>
      <td>Oct 2</td>
      <td>228.07</td>
      <td>232.78</td>
      <td>229.49</td>
      <td>233.52</td>
      <td>218.58</td>
      <td>226.00</td>
      <td>37445848</td>
      <td>36370828</td>
    </tr>
    <tr>
      <th>2019-10-03</th>
      <td>1.94</td>
      <td>-0.014334</td>
      <td>0.8574</td>
      <td>231.74</td>
      <td>225.67</td>
      <td>Oct 3</td>
      <td>217.92</td>
      <td>221.74</td>
      <td>231.50</td>
      <td>225.57</td>
      <td>224.30</td>
      <td>222.75</td>
      <td>31557655</td>
      <td>30834853</td>
    </tr>
    <tr>
      <th>2019-10-04</th>
      <td>6.46</td>
      <td>0.014193</td>
      <td>2.8351</td>
      <td>230.52</td>
      <td>234.07</td>
      <td>Oct 4</td>
      <td>225.19</td>
      <td>228.58</td>
      <td>237.81</td>
      <td>237.88</td>
      <td>226.40</td>
      <td>227.52</td>
      <td>35754280</td>
      <td>34896043</td>
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
iex.init(key.test_token, api='sandbox')
# iex.init(key.token, api='cloud')
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
