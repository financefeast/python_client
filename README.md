# Financefeast

A client library to call the Financefeast API

Note: this is alpha quality code still, the API may change, and things may fall apart while you try it.

# Quick start

## Installation

`financefeast` is available from [pypi](https://pypi.org/project/{INSERT ME HERE}/) so you can install it as usual:

```
$ pip install financefeast
```

## Usage
You must supply your client id and client secret. Two ways, either when you create an instance of Financefeast by passing
client_id and client_secret as args.

```
client = FinanceFeast(client_id="SOME ID", client_secret="SOME SECRET")
```

or

Using environment variables CLIENT_ID and CLIENT_SECRET.

```
client = FinanceFeast()
```

### Example
```python
from financefeast import FinanceFeast

client = FinanceFeast(client_id="your_client_id", 
                      client_secret="your_client_secret")
print(client.tickers())
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
