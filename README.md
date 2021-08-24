# Financefeast

A client library to call the Financefeast API

Note: this is alpha quality code still, the API may change, and things may fall apart while you try it.

# Quick start

## Installation

`financefeast` is available from [pypi](https://pypi.org/project/financefeast/) so you can install it as usual:

```
$ pip install financefeast
```

## API Reference
The API reference documentation can be found [here](https://doc.financefeast.io/api-documentation/api-v1/)

## Usage
You must supply one of either :
* Your client id and client secret. You can do this one of two ways, either when you create an instance of Financefeast by passing
   client_id and client_secret as args.
   ```
   client = FinanceFeast(client_id="SOME ID", client_secret="SOME SECRET")
   ```
   
   *or*
   
   Using environment variables 
   ```
   FF-CLIENT-ID and FF-CLIENT-SECRET
   ```
   and then
   ```
   client = FinanceFeast()
   ```
* A valid access token
   ```
   client = FinanceFeast(token="SOME ACCESS TOKEN")
   ```


### Example

```python
from financefeast import Rest

client = Rest(client_id="your_client_id",
              client_secret="your_client_secret")
print(client.tickers().data)
```

or

```python
from financefeast import Rest

client = Rest(token="0Coreo505Xcm46*xkrj$sodm232s")
print(client.tickers().data)
```


## Endpoints

Notes:
* For endpoints that have date query parameters, if these are not passed then the default will be the current day, except
 for financial endpoints where the date will default to the current calendar year.
* Ticker query parameter can either be a symbol or uuid4 string. The uuid4 string is explict, where the symbol could be
 in multiple exchanges. If the exchange query parameter is also passed with symbol then that would be explict also.


### validate
Validate your token. Returns 'true' if valid and not expired, otherwise 'false'
Query params : None
```python
print(client.validate())
```
### alive
Check API health.
Query params : None
```python
print(client.alive())
```
### usage
Get account endpoint usage by endpoint, and count by day
Query params :
* date_from: string ; date range start in format YYYY-MM-DD
* date_to: string ; date range end in format YYYY-MM-DD
```python
print(client.usage(date_from="2021-04-01"))
```
### tickers
Get a list of supported tickers
Query params :
* exchange: string ; limit tickers to this exchange
```python
print(client.tickers().data)
```
### tickers_search
Get a list of supported tickers
Query params :
* search_str: string ; search for a ticker symbol, uuid4 or company name. Partials will match and case insensitive
* exchange: string ; limit tickers to this exchange
```python
print(client.tickers_search(search_str="1d72e892-7336-4097-a762-7a9680111721"))
```
### exchange
Get a list of supported exchanges
Query params : None
```python
print(client.exchange().data)
```
### exchange_status
Get the current status of the exchange, either open or closed.
* exchange: string ; query this exchange
```python
print(client.exchange_status(exchange="nzx"))
```
### social_sentiment
Get social media sentiment for ticker
Query params :
* ticker: string ; symbol or uuid4 of stock to return prices (required)
* date_from: string ; date range start in format YYYY-MM-DD
* date_to: string ; date range end in format YYYY-MM-DD
* exchange: string ; exchange ticker is member of
* platform: string ; limit search to a social media platform, eg twitter
```python
print(client.social_sentiment(ticker="air.nz", date_from="2021-01-01", date_to="2021-02-01"))
```
### cpi
Get "consumer price index" data
Query params :
* date_from: string ; date range start in format YYYY-MM-DD
* date_to: string ; date range end in format YYYY-MM-DD
* year: string ; year to search data for in format YYYY
```python
print(client.cpi(date_from="2021-01-01", date_to="2021-02-01"))
```
### eod
Get "end of day" prices for ticker
Query params :
* ticker: string ; symbol or uuid4 of stock to return prices (required)
* date_from: string ; date range start in format YYYY-MM-DD
* date_to: string ; date range end in format YYYY-MM-DD
* exchange: string ; exchange ticker is member of
* interval: string ; date time interval
```python
print(client.eod('air.nz', date_from='2020-11-01', date_to='2020-11-29'))
```
### intraday
Get "intraday" prices for ticker
Query params :
* ticker: string ; symbol or uuid4 of stock to return prices (required)
* datetime_from: string ; date range start in format YYYY-MM-DD : hh:mm:ss
* datetime_to: string ; date range end in format YYYY-MM-DD : hh:mm:ss
* exchange: string ; exchange ticker is member of
* interval: string ; date time interval
```python
print(client.intraday('air.nz', datetime_from='2020-11-01', datetime_to='2020-11-29'))
```
### last
Get "last" price record for ticker
Query params :
* ticker: string ; symbol or uuid4 of stock to return prices (required)
* exchange: string ; exchange ticker is member of
```python
print(client.last('air.nz'))
```
### orderbook
Get an "orderbook" showing level 2 data for a ticker
Query params :
* ticker: string ; symbol or uuid4 of stock to return prices (required)
* condensed: bool ; true for condensed orderbook or false for full. defaults to true to return a condensed response
* exchange: string ; exchange ticker is member of
```python
print(client.orderbook('air.nz', condensed=False))
```
### sma
Get "sma" prices and simple moving average for ticker
Query params :
* ticker: string ; symbol or uuid4 of stock to return prices (required)
* datetime_from: string ; date range start in format YYYY-MM-DD : hh:mm:ss
* datetime_to: string ; date range end in format YYYY-MM-DD : hh:mm:ss
* exchange: string ; exchange ticker is member of
* interval: string ; date time interval
* window: list ; list of integers for the sma look-back window
```python
print(client.sma('air.nz', datetime_from='2021-08-01', datetime_to='2021-08-05'))
```
### ema
Get "ema" prices and exponential moving average for ticker
Query params :
* ticker: string ; symbol or uuid4 of stock to return prices (required)
* datetime_from: string ; date range start in format YYYY-MM-DD : hh:mm:ss
* datetime_to: string ; date range end in format YYYY-MM-DD : hh:mm:ss
* exchange: string ; exchange ticker is member of
* interval: string ; date time interval
* window: list ; list of integers for the ema look-back window
```python
print(client.ema('air.nz', datetime_from='2020-11-01', datetime_to='2020-11-29'))
```
### macd
Get "macd" prices and moving average convergence divergence for ticker
Query params :
* ticker: string ; symbol or uuid4 of stock to return prices (required)
* datetime_from: string ; date range start in format YYYY-MM-DD : hh:mm:ss
* datetime_to: string ; date range end in format YYYY-MM-DD : hh:mm:ss
* exchange: string ; exchange ticker is member of
* interval: string ; date time interval
```python
print(client.macd('air.nz', datetime_from='2020-11-01', datetime_to='2020-11-29'))
```
### rsi
Get "rsi" prices and relative strength indicator for ticker
Query params :
* ticker: string ; symbol or uuid4 of stock to return prices (required)
* datetime_from: string ; date range start in format YYYY-MM-DD : hh:mm:ss
* datetime_to: string ; date range end in format YYYY-MM-DD : hh:mm:ss
* exchange: string ; exchange ticker is member of
* interval: string ; date time interval
* window: list ; list of integers for the rsi look-back window
```python
print(client.rsi('air.nz', datetime_from='2020-11-01', datetime_to='2020-11-29'))
```
### adx
Get "adx" prices and average directional index for ticker
Query params :
* ticker: string ; symbol or uuid4 of stock to return prices (required)
* datetime_from: string ; date range start in format YYYY-MM-DD : hh:mm:ss
* datetime_to: string ; date range end in format YYYY-MM-DD : hh:mm:ss
* exchange: string ; exchange ticker is member of
* interval: string ; date time interval
* window: integer ; integer for the adx first sliding look-back window
* window_adx: integer ; integer for the adx last sliding look-back window
```python
print(client.adx('air.nz', datetime_from='2020-11-01', datetime_to='2020-11-29'))
```
### bollinger
Get "bollinger" prices and bollinger band for ticker
Query params :
* ticker: string ; symbol or uuid4 of stock to return prices (required)
* datetime_from: string ; date range start in format YYYY-MM-DD : hh:mm:ss
* datetime_to: string ; date range end in format YYYY-MM-DD : hh:mm:ss
* exchange: string ; exchange ticker is member of
* interval: string ; date time interval
* window: list ; list of integers for the bollinger look-back window
```python
print(client.bollinger('air.nz', datetime_from='2020-11-01', datetime_to='2020-11-29'))
```
### stochastic
Get "stochastic" prices and stochastic oscillator for ticker
Query params :
* ticker: string ; symbol or uuid4 of stock to return prices (required)
* datetime_from: string ; date range start in format YYYY-MM-DD : hh:mm:ss
* datetime_to: string ; date range end in format YYYY-MM-DD : hh:mm:ss
* exchange: string ; exchange ticker is member of
* interval: string ; date time interval
* window: integer ; integer for the stochastic look-back window
```python
print(client.stochastic('air.nz', datetime_from='2020-11-01', datetime_to='2020-11-29'))
```
### cashflow
Get "cashflow" financial data for ticker
Query params :
* ticker: string ; symbol or uuid4 of stock to return data (required)
* date_from: string ; date range start in format YYYY-MM-DD
* date_to: string ; date range end in format YYYY-MM-DD
* year: string ; year to search data for in format YYYY
* exchange: string ; exchange ticker is member of
```python
print(client.cashflow('air.nz', year=2020))
```
### income
Get "income" financial data for ticker
Query params :
* ticker: string ; symbol or uuid4 of stock to return data (required)
* date_from: string ; date range start in format YYYY-MM-DD
* date_to: string ; date range end in format YYYY-MM-DD
* year: string ; year to search data for in format YYYY
* exchange: string ; exchange ticker is member of
```python
print(client.income('air.nz', year=2020))
```
### balance
Get "balance sheet" financial data for ticker
Query params :
* ticker: string ; symbol or uuid4 of stock to return data (required)
* date_from: string ; date range start in format YYYY-MM-DD
* date_to: string ; date range end in format YYYY-MM-DD
* year: string ; year to search data for in format YYYY
* exchange: string ; exchange ticker is member of
```python
print(client.balance('air.nz', year=2020))
```
### dividend
Get "dividend payout" data for ticker
Query params :
* ticker: string ; symbol or uuid4 of stock to return data (required)
* date_from: string ; date range start in format YYYY-MM-DD
* date_to: string ; date range end in format YYYY-MM-DD
* year: string ; year to search data for in format YYYY
* exchange: string ; exchange ticker is member of
```python
print(client.dividend('air.nz', year=2020))
```
### split
Get "split ratio" data for ticker
Query params :
* ticker: string ; symbol or uuid4 of stock to return data (required)
* date_from: string ; date range start in format YYYY-MM-DD
* date_to: string ; date range end in format YYYY-MM-DD
* year: string ; year to search data for in format YYYY
* exchange: string ; exchange ticker is member of
```python
print(client.split('air.nz', year=2020))
```
# Features

All API endpoints are supported, plus detection of ratelimiting.

Supported now:

- All routes
- Rate limit aware
- Authorization

Future:

- Backoff when approaching rate limit thresholds

# Limitations and known issues

None at this time.

# Developing and contributing

## Building wheel
```
python setup.py bdist_wheel
```

## Installing wheel
```
pip install /path/to/wheelfile.whl
```

PRs are more than welcome! Please include tests for your changes :)

# History
|Version|Description
|------ |-----------
|0.0.25|- Refactored 'exchanges' method to 'exchage' to align with actual API endpoint<br>- Corrected all technical indicator methods datetime_from and datetime_to parameters. These were not passing the correct parameter names to the API
|0.0.24|- Added 'cpi' method for the new consumer price index API endpoint