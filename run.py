from financefeast.client import FinanceFeast


client = FinanceFeast()

# alive
#print(client.alive())

#tickers
#print(client.tickers())

#exchanges
#print(client.exchanges())

# end of day
#print(client.eod('air.nz', date_from='2020-11-01', date_to='2020-11-29'))

# intra day
print(client.intraday('air.nz', datetime_from='2020-11-01', datetime_to='2020-11-29'))

