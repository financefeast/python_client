from enum import Enum

class Environments(Enum):
    local = "http://localhost:5005"
    test = "https://api.test.financefeast.io"
    prod = "https://api.financefeast.io"

class EnvironmentsStream(Enum):
    local = "ws://localhost:5005/ws"
    test = "wss://stream.test.financefeast.io/ws"
    prod = "wss://stream.financefeast.io/ws"