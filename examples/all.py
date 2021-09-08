from financefeast.rest import Rest, Environments

"""
    Remember to see your API token environment variable!
        FF-TOKEN

    or supply a token=XXX using token parameter when creating the Financefeast instance
"""

client = Rest(environment=Environments.prod)

# validate
print(client.validate())

# alive
#print(client.alive())

# usage
#print(client.usage(date_from="2021-04-01"))

#tickers
#print(client.tickers().data)

#tickers_search
#print(client.tickers_search(search_str="1d72e892-7336-4097-a762-7a9680111721"))

#exchange
#print(client.exchange().data)

#exchange_status
#print(client.exchange_status(exchange="nzx").data)

# end of day
#print(client.eod('air.nz', date_from='2020-11-01', date_to='2020-11-29'))

# intra day
#print(client.intraday('air.nz', datetime_from='2020-11-01', datetime_to='2020-11-29'))

# simple moving average
#print(client.sma('air.nz', datetime_from='2021-08-01', datetime_to='2021-08-05'))

# exponential moving average
#print(client.ema('air.nz', datetime_from='2020-11-01', datetime_to='2020-11-29'))

# macd
#print(client.macd('air.nz', datetime_from='2020-11-01', datetime_to='2020-11-29'))

# rsi
#print(client.rsi('air.nz', datetime_from='2020-11-01', datetime_to='2020-11-29'))

# adx
#print(client.adx('air.nz', datetime_from='2020-11-01', datetime_to='2020-11-29'))

# bollinger
#print(client.bollinger('air.nz', datetime_from='2020-11-01', datetime_to='2020-11-29'))

# stochastic
#print(client.stochastic('air.nz', datetime_from='2020-11-01', datetime_to='2020-11-29'))

# balance
#print(client.balance('air.nz', year=2020))

# balance
#print(client.announcement('air.nz', year=2021))