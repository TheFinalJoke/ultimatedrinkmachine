#!/usr/bin/env python3 

import socket
import pickle
import time
from lib.base import BaseDrinkClass
from lib.protocol import DrinkClientSocket
from lib.protocol import DrinkProtocol
#from lib.protocol import Alcohol_to_Pump

base_recipe = DrinkProtocol()
recipes = [
    base_recipe.transform("gin and tonic", 40, 40, 5),
    #base_recipe.transform("Whiskey Coke", Alcohol_to_Pump.WHISKEY.name, Alcohol_to_Pump.COKE.name, 4),
    #base_recipe.transform("Vodka Sprite", Alcohol_to_Pump.VODKA.name, Alcohol_to_Pump.SPRITE.name, 1),
    #base_recipe.transform("Bourbon Coke", Alcohol_to_Pump.BOURBON.name, Alcohol_to_Pump.COKE.name, 5),
    #base_recipe.transform("CLEAN CYCLE FINISHED", "CLEANER", "CLEANER", 25)
    ]


for recipe in recipes:
    drinksock = DrinkClientSocket()
    drinksock.connect()
    recv = drinksock.send_data(recipe)
    print(recv)

print("DONE")
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