from financefeast.stream import Stream, EnvironmentsStream

def on_data(stream, data):
    print(data)

client = Stream(token='some_token', on_data=on_data, environment=EnvironmentsStream.local)
client.connect()