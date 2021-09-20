from enum import Enum

class Environments(Enum):
    local = "http://localhost:5005"
    test = "https://api.test.financefeast.io"
    prod = "https://api.financefeast.io"

class EnvironmentsStream(Enum):
    local = "ws://localhost:5005/ws"
    test = "ws://stream.test.financefeast.io/ws"
    prod = "ws://stream.financefeast.io/ws"