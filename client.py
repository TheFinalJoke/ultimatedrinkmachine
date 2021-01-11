#!/usr/bin/env python3 

import socket
import pickle
import time
from lib.base import BaseDrinkClass
from lib.protocol import DrinkClientSocket
from lib.protocol import DrinkProtocol
from lib.protocol import Alcohol_to_Pump

base_recipe = DrinkProtocol()

recipe = base_recipe.transform("gin and tonic", Alcohol_to_Pump.COKE.name, Alcohol_to_Pump.GIN.name, 3)

drinksock = DrinkClientSocket()

drinksock.connect()

recv = drinksock.send_data(recipe)

print(recv)
"""
class hello_server():
    def __init__(self) -> None:
        super().__init__()
    def hello(self):
        return "hello From stuff"

while True:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(('127.0.0.1', 29888))
    hello = bytes("hello from client 1", "utf-8")
    server_socket.sendall(hello)
    data = server_socket.recv(1024)
    print(repr(data))
    time.sleep(1)
    continue

server_socket.close()
"""