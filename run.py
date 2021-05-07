from financefeast.client import FinanceFeast, Environments

"""
    Remember to see some environment variables!
        FF-CLIENT-ID
        FF-CLIENT-SECRET
        
    or supply client_id and client_token as parameters
    
    or supply a token using token parameter
"""

client = FinanceFeast(environment=Environments.prod)

# validate
#print(client.validate())

# alive
#print(client.alive())

# usage
#print(client.usage(date_from="2021-04-01"))

#tickers
#print(client.tickers())

#tickers_search
#print(client.tickers_search(search_str="1d72e892-7336-4097-a762-7a9680111721"))


#exchanges
#print(client.exchanges())

# end of day
#print(client.eod('air.nz', date_from='2020-11-01', date_to='2020-11-29'))

# intra day
#print(client.intraday('air.nz', datetime_from='2020-11-01', datetime_to='2020-11-29'))

# simple moving average
#print(client.sma('air.nz', datetime_from='2020-11-01', datetime_to='2020-11-29'))

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