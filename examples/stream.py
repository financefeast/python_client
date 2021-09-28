from financefeast.stream import Stream, EnvironmentsStream

def on_data(stream, data):
    print(data)

client = Stream(token='your_token', on_data=on_data)
client.connect()