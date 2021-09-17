from financefeast.stream import Stream, EnvironmentsStream

client = Stream(token='sdsds', environment=EnvironmentsStream.local)
client.connect()