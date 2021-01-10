#!/usr/bin/env python3

from enum import Enum
import enum
import socket
from lib.base import BaseDrinkClass

HEADER = 10
# Might have to write to disk 
alcohol_list = []

class Alcohol_to_Pump(Enum):
    GIN=1
    WHISKEY=2
    COKE=3
    TONIC=4

class DrinkClientSocket(BaseDrinkClass):
    def __init__(self, sock=None) -> None:
        super().__init__()
        if sock == None:
            self.sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )
        else:
            self.sock = sock

    def connect(self, host=socket.gethostname(), port=29888):
        self.debug(f"Attempting to connect to {host}, {port}")
        self.sock.connect((host, port))

    def send_data(self, data):
        pass 
    
    def recd_data(self):
        pass
    
class DrinkServerSocket(BaseDrinkClass):
    def __init__(self, sock=None) -> None:
        super().__init__()
        if sock == None:
            self.sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )
        else:
            self.sock = sock

    def bind_and_listen(self, host=socket.gethostname(), port=29888):
        self.debug(f"Attempting to bind and listen on {host}, {port}")
        self.sock.bind((host, port))
        # Should not have more than 5 requests at a time   
        self.sock.listen(5)
    
class DrinkProtocol(BaseDrinkClass):
    """
    Packages data to send it over to the server
    Input ?

    Output Json
    ex 
    Name: Str
    Drink1: ENUM STR->Pump #
    Drink2: ENUM STR->Pump #
    Strength: int -> How strong the drink will be
    {Drink: [{name: GinandTonic}, {drink1: gin}, 
            {drink2: tonic}, {strength: 3}]}
    """
    def alcohol_checker():
        pass
    @staticmethod
    def transform(name, alcohol, mixer, strength):
        pass
