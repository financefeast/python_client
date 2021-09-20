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

# Rest Client

## Usage
To authenticate to the API you must supply your API authentication token which can be obtained from your [API Dashboard](https://financefeast.io/#creds)

The token can be supplied by either:
* Passing your token when creating an instance of Financefeast as
    ```python
    client = Rest(token="SOME TOKEN")
    ```
* As an environment variable FF-TOKEN
    ```commandline
    FF-TOKEN="SOME TOKEN"
    client = Rest()
    ```

## Client Credentials (DEPRECIATED)
Client credentials using the client ID and client Secret are depreciated and will be removed from a future release. You can at the present time
use this authentication method to allow time to upgrade your applications. 

NOTE: When using the new API authentication tokens, you no longer need to `login` to the API.

You must supply one of either :
* Your client id and client secret. You can do this one of two ways, either when you create an instance of Financefeast by passing
   client_id and client_secret as args.
   ```
   client = Rest(client_id="SOME ID", client_secret="SOME SECRET")
   ```
   
   *or*
   
   Using environment variables 
   ```
   FF-CLIENT-ID and FF-CLIENT-SECRET
   ```
   and then
   ```
   client = Rest()
   ```
* A valid access token
   ```
   client = Rest(token="SOME ACCESS TOKEN")
   ```


### Example

```python
from financefeast import Rest

client = Rest(token="SOME_TOKEN")
print(client.tickers().data)
```


## Endpoints

Notes:
* For endpoints that have date query parameters, if these are not passed then the default will be the current day, except
 for financial endpoints where the date will default to the current calendar year.
* Ticker query parameter can either be a symbol or uuid4 string. The uuid4 string is explict, where the symbol could be
 in multiple exchanges. If the exchange query parameter is also passed with symbol, then that would be explict also.


### validate
Validate your token. Returns 'true' if valid and not expired, otherwise 'false'<br>
Query params : None
```python
print(client.validate())
```
### alive
Check API health.<br>
Query params : None
```python
print(client.alive())
```
### usage
Get account endpoint usage by endpoint, and count by day<br>
Query params :
* date_from: string ; date range start in format YYYY-MM-DD
* date_to: string ; date range end in format YYYY-MM-DD
```python
print(client.usage(date_from="2021-04-01"))
```
### tickers
Get a list of supported tickers<br>
Query params :
* exchange: string ; limit tickers to this exchange
```python
print(client.tickers().data)
```
### tickers_search
Get a list of supported tickers<br>
Query params :
* search_str: string ; search for a ticker symbol, uuid4 or company name. Partials will match and case insensitive
* exchange: string ; limit tickers to this exchange
```python
print(client.tickers_search(search_str="1d72e892-7336-4097-a762-7a9680111721"))
```
### exchange
Get a list of supported exchanges<br>
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
Get social media sentiment for ticker<br>
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
Get "consumer price index" data<br>
Query params :
* date_from: string ; date range start in format YYYY-MM-DD
* date_to: string ; date range end in format YYYY-MM-DD
* year: string ; year to search data for in format YYYY
```python
print(client.cpi(date_from="2021-01-01", date_to="2021-02-01"))

### announcement
Get company announcements for ticker<br>
Query params :
* ticker: string ; symbol or uuid4 of stock to return prices (required)
* date_from: string ; date range start in format YYYY-MM-DD
* date_to: string ; date range end in format YYYY-MM-DD
* exchange: string ; exchange ticker is member of
* year: string ; year to search data for in format YYYY
```python
print(client.announcement(ticker="air.nz", date_from="2021-01-01", date_to="2021-02-01"))

```
### eod
Get "end of day" prices for ticker<br>
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
Get "intraday" prices for ticker<br>
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
Get "last" price record for ticker<br>
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
Get "sma" prices and simple moving average for ticker<br>
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
Get "ema" prices and exponential moving average for ticker<br>
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
Get "macd" prices and moving average convergence divergence for ticker<br>
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
Get "rsi" prices and relative strength indicator for ticker<br>
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
Get "adx" prices and average directional index for ticker<br>
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
Get "bollinger" prices and bollinger band for ticker<br>
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
Get "stochastic" prices and stochastic oscillator for ticker<br>
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
Get "cashflow" financial data for ticker<br>
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
Get "income" financial data for ticker<br>
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
Get "balance sheet" financial data for ticker<br>
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
Get "dividend payout" data for ticker<br>
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
Get "split ratio" data for ticker<br>
Query params :
* ticker: string ; symbol or uuid4 of stock to return data (required)
* date_from: string ; date range start in format YYYY-MM-DD
* date_to: string ; date range end in format YYYY-MM-DD
* year: string ; year to search data for in format YYYY
* exchange: string ; exchange ticker is member of
```python
print(client.split('air.nz', year=2020))
```

# Stream

The Stream client connects to the Financefeast Stream API using websockets. This is a feature of some of the paid subscription plans and
streams in real-time price updates received from the exchange. It's as real-time as you can get.

## Usage

Instantiate the class Stream, passing in parameters `token` and a callback object `on_data`. The callback object or method will be passed
the received data from the Stream API in json format. If no callback method is passed data will be logged to stdout as a string.

```python
from financefeast.stream import Stream, EnvironmentsStream

def on_data(stream, data):
    print(data)

client = Stream(token='your_api_token', on_data=on_data, environment=EnvironmentsStream.local)
client.connect()
```

### Notes
* The Stream class will auto-reconnect on a dropped connection.
* It will authenticate to the Stream API and if unsuccessful the Stream API will drop the socket and return an error to the client.
* It will run forever until terminated.
* All subscription plans have a maximum concurrent streams limit. If you attempt to open a stream above your limit it will be rejected
with an error message.

# Features of the Client

All API endpoints are supported, plus detection of ratelimiting. Streaming is also included.

Supported now:

- All routes
- Rate limit aware
- Authorization
- Streaming via websockets

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
|0.0.29|- Updated stream endpoint paths
|0.0.28|- Stream class added to consume Financefeast Stream API
|0.0.27|- Client credentials depreciated. Now using API authentication tokens for authentication to the API.
|0.0.26|- Added company announcements 'announcement' endpoint.
|0.0.25|- Refactored 'exchanges' method to 'exchange' to align with actual API endpoint<br>- Corrected all technical indicator methods datetime_from and datetime_to parameters. These were not passing the correct parameter names to the API
|0.0.24|- Added 'cpi' method for the new consumer price index API endpoint