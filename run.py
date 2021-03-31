from financefeast.client import FinanceFeast




client = FinanceFeast(client_id="OBhYDnjl1hKwmPyaobIzzhNg", client_secret="Yus1shSvo2xuEBIZJNBxZH0XQ6XdCE0FhEdQ9dujzZ9Vi8VC")

# alive
print(client.alive())
#tickers
print(client.tickers())
#exchanges
print(client.exchanges())