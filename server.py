"""
pyzmq thermo example
"""
import time
import zmq
from CoolProp.CoolProp import PropsSI


def propssi(msg: dict):
    """
    PropsSI implementation
    """
    property1 = msg["property1"]
    property2 = msg["property2"]
    value1 = msg["value1"]
    value2 = msg["value2"]
    fluid = msg["fluid"]
    return {
        "T": PropsSI("T", property1, value1, property2, value2, fluid),
        "P": PropsSI("P", property1, value1, property2, value2, fluid),
        "D": PropsSI("D", property1, value1, property2, value2, fluid),
        "H": PropsSI("H", property1, value1, property2, value2, fluid),
        "S": PropsSI("S", property1, value1, property2, value2, fluid),
        "Q": PropsSI("Q", property1, value1, property2, value2, fluid),
    }


context = zmq.Context()
socket = context.socket(zmq.REP)

socket.bind("tcp://*:5555")

while True:
    # receive message as json
    message = socket.recv_json()
    print(message)
    if message["type"] == "property":
        socket.send_json(propssi(message))
    else:
        socket.send_json({"error": "unknown type"})
    time.sleep(0.1)
