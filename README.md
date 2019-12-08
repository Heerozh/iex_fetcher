

# Simple IEX Stock Fetcher

A python lib to get stock prices/dividends/splits from IEX Cloud.

My IEX Referrals: [https://iexcloud.io/s/62efba08](https://iexcloud.io/s/62efba08)

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



## Fetcher stocks


```python
symbols = iex.Reference.symbols()
symbols = symbols[(symbols.type == 'ad') | (symbols.type == 'cs') & (symbols.exchange != 'OTC')]
symbols = symbols.symbol.values
```


```python
from tqdm.notebook import tqdm
for k in tqdm(symbols):
    sys.stdout.write('\r{}   '.format(k))
    filename = "./daily/{}.csv".format(k)
    iex.Stock(k).chart('5y').to_csv(filename)
print('ok')
```

Code above will consume about 60 million messages


