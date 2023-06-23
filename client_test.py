"""
pyzmq thermo example
"""

import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)

socket.connect("tcp://localhost:5555")

message = {
    "type": "property",
    "property1": "P",
    "property2": "Q",
    "value1": 101325.0,
    "value2": 0.5,
    "fluid": "Water",
}

socket.send_json(message)
message = socket.recv_json()
print(message)
