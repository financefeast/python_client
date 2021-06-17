# Financefeast

A client library to call the Financefeast API

Note: this is alpha quality code still, the API may change, and things may fall apart while you try it.

# Quick start

## Installation

`financefeast` is available from [pypi](https://pypi.org/project/financefeast/) so you can install it as usual:

```
$ pip install financefeast
```

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
print(client.tickers())
```

or

```python
from financefeast import Rest

client = Rest(token="0Coreo505Xcm46*xkrj$sodm232s")
print(client.tickers())
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

### alive
Check API health.
Query params : None

### usage
Get account endpoint usage by endpoint, and count by day
Query params :
* date_from: string ; date range start in format YYYY-MM-DD
* date_to: string ; date range end in format YYYY-MM-DD

### tickers
Get a list of supported tickers
Query params :
* exchange: string ; limit tickers to this exchange

### tickers_search
Get a list of supported tickers
Query params :
* search_str: string ; search for a ticker symbol, uuid4 or company name. Partials will match and case insensitive
* exchange: string ; limit tickers to this exchange

### exchanges
Get a list of supported exchanges
Query params : None

### eod
Get "end of day" prices for ticker
Query params :
* ticker: string ; symbol or uuid4 of stock to return prices (required)
* date_from: string ; date range start in format YYYY-MM-DD
* date_to: string ; date range end in format YYYY-MM-DD
* exchange: string ; exchange ticker is member of
* interval: string ; data time interval

### intraday
Get "intraday" prices for ticker
Query params :
* ticker: string ; symbol or uuid4 of stock to return prices (required)
* datetime_from: string ; date range start in format YYYY-MM-DD : hh:mm:ss
* datetime_to: string ; date range end in format YYYY-MM-DD : hh:mm:ss
* exchange: string ; exchange ticker is member of
* interval: string ; data time interval

### sma
Get "sma" prices and simple moving average for ticker
Query params :
* ticker: string ; symbol or uuid4 of stock to return prices (required)
* datetime_from: string ; date range start in format YYYY-MM-DD : hh:mm:ss
* datetime_to: string ; date range end in format YYYY-MM-DD : hh:mm:ss
* exchange: string ; exchange ticker is member of
* interval: string ; data time interval
* window: list ; list of integers for the sma lookback window

### ema
Get "ema" prices and exponential moving average for ticker
Query params :
* ticker: string ; symbol or uuid4 of stock to return prices (required)
* datetime_from: string ; date range start in format YYYY-MM-DD : hh:mm:ss
* datetime_to: string ; date range end in format YYYY-MM-DD : hh:mm:ss
* exchange: string ; exchange ticker is member of
* interval: string ; data time interval
* window: list ; list of integers for the ema lookback window

### macd
Get "macd" prices and moving average convergence divergence for ticker
Query params :
* ticker: string ; symbol or uuid4 of stock to return prices (required)
* datetime_from: string ; date range start in format YYYY-MM-DD : hh:mm:ss
* datetime_to: string ; date range end in format YYYY-MM-DD : hh:mm:ss
* exchange: string ; exchange ticker is member of
* interval: string ; data time interval

### rsi
Get "rsi" prices and relative strength indicator for ticker
Query params :
* ticker: string ; symbol or uuid4 of stock to return prices (required)
* datetime_from: string ; date range start in format YYYY-MM-DD : hh:mm:ss
* datetime_to: string ; date range end in format YYYY-MM-DD : hh:mm:ss
* exchange: string ; exchange ticker is member of
* interval: string ; data time interval
* window: list ; list of integers for the rsi lookback window

### adx
Get "adx" prices and average directional index for ticker
Query params :
* ticker: string ; symbol or uuid4 of stock to return prices (required)
* datetime_from: string ; date range start in format YYYY-MM-DD : hh:mm:ss
* datetime_to: string ; date range end in format YYYY-MM-DD : hh:mm:ss
* exchange: string ; exchange ticker is member of
* interval: string ; data time interval
* window: integer ; integer for the adx first sliding lookback window
* window_adx: integer ; integer for the adx last sliding lookback window

### bollinger
Get "bollinger" prices and bollinger band for ticker
Query params :
* ticker: string ; symbol or uuid4 of stock to return prices (required)
* datetime_from: string ; date range start in format YYYY-MM-DD : hh:mm:ss
* datetime_to: string ; date range end in format YYYY-MM-DD : hh:mm:ss
* exchange: string ; exchange ticker is member of
* interval: string ; data time interval
* window: list ; list of integers for the bollinger lookback window

### stochastic
Get "stochastic" prices and stochastic oscillator for ticker
Query params :
* ticker: string ; symbol or uuid4 of stock to return prices (required)
* datetime_from: string ; date range start in format YYYY-MM-DD : hh:mm:ss
* datetime_to: string ; date range end in format YYYY-MM-DD : hh:mm:ss
* exchange: string ; exchange ticker is member of
* interval: string ; data time interval
* window: integer ; integer for the stochastic lookback window

### cashflow
Get "cashflow" financial data for ticker
Query params :
* ticker: string ; symbol or uuid4 of stock to return data (required)
* date_from: string ; date range start in format YYYY-MM-DD
* date_to: string ; date range end in format YYYY-MM-DD
* year: string ; year to search data for in format YYYY
* exchange: string ; exchange ticker is member of

### income
Get "income" financial data for ticker
Query params :
* ticker: string ; symbol or uuid4 of stock to return data (required)
* date_from: string ; date range start in format YYYY-MM-DD
* date_to: string ; date range end in format YYYY-MM-DD
* year: string ; year to search data for in format YYYY
* exchange: string ; exchange ticker is member of

### balance
Get "balance sheet" financial data for ticker
Query params :
* ticker: string ; symbol or uuid4 of stock to return data (required)
* date_from: string ; date range start in format YYYY-MM-DD
* date_to: string ; date range end in format YYYY-MM-DD
* year: string ; year to search data for in format YYYY
* exchange: string ; exchange ticker is member of

### dividend
Get "dividend payout" data for ticker
Query params :
* ticker: string ; symbol or uuid4 of stock to return data (required)
* date_from: string ; date range start in format YYYY-MM-DD
* date_to: string ; date range end in format YYYY-MM-DD
* year: string ; year to search data for in format YYYY
* exchange: string ; exchange ticker is member of

### split
Get "split ratio" data for ticker
Query params :
* ticker: string ; symbol or uuid4 of stock to return data (required)
* date_from: string ; date range start in format YYYY-MM-DD
* date_to: string ; date range end in format YYYY-MM-DD
* year: string ; year to search data for in format YYYY
* exchange: string ; exchange ticker is member of

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
