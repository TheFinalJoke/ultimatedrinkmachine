#!/usr/bin/env python3

import json
import sqlite3
import socket
from enum import Enum
import pdb
from lib.talking import (
    Accessor,
    FormulateViewQuery
)
from django.db import connection

from lib.base import BaseDrinkClass

#HEADER = 10
# Might have to write to disk
DBPATH = "/home/nickshorter/ultimatedrinkmachine/www/ultimatedrinkmachine/db.sqlite3"
accessor = Accessor(DBPATH)
view_query = FormulateViewQuery.query("selections_recipe")
results = accessor.execute(view_query)
pdb.set_trace()
ALCOHOL_TO_PUMP = []

class DrinkException(Exception):
    pass

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
        self.HEADER = 10

    def connect(self, host='127.0.0.1', port=29888):
        self.debug(f"Attempting to connect to {host}, on port {port}")
        self.sock.connect((host, port))

    def build_with_buffersize(self, msg):
        return bytes(msg, "utf-8")

    def send_data(self, data: str):
        """
        It should take in a STR json object

        """

        data_with_buffer = self.build_with_buffersize(data)
        self.sock.sendall(data_with_buffer)

        full_mesg_back = ""
        new_msg = True
        while True:
            msg = self.sock.recv(1024)
            if new_msg:
                msglen = int(len(msg[:self.HEADER]))
                new_msg = False
            full_mesg_back += msg.decode('utf-8')
            if len(full_mesg_back)-self.HEADER == msglen:
                self.debug("recieved full message")
                new_msg = True
            else:
                return full_mesg_back

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
            self.header = 10

    def bind_and_listen(self, host='127.0.0.1', port=29888):
        self.debug(f"Attempting to bind and listen on {host}, on port {port}")
        self.sock.bind((host, port))
        # Should not have more than 5 requests at a time   
        self.sock.listen(5)
        return self.sock
    
    def accept(self):
        while True:
            clientsocket, address = self.sock.accept()
            data = clientsocket.recv(1024)
            self.info(f"Data recieved {data} from {address}")
            clientsocket.send(bytes(f"Data Accepted from {address}", "utf-8"))

    
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
    {NAME: GinandTonic, ALCOHOL: gin, 
            MIXER: tonic, STRENGTH: 3}
    """
    def __init__(self) -> None:
        super().__init__()

    def liquid_checker(self, liquid):
        """
        Checks Against the Enum to make sure
        Liquid has a pump number too it
        """
        return liquid in Alcohol_to_Pump.__members__

    def transform(self, name, alcohol, mixer, strength):
        """
        Gets Instructions and makes a receipe

        Returns STR For easy json
        """
        try:
            if not self.liquid_checker(alcohol) or not self.liquid_checker(mixer):
                raise DrinkException("Op I'm Drunk, I mean its not in the enum")
            drink_dict = {
                        "NAME": name,
                        "ALCOHOL": alcohol,
                        "MIXER": mixer,
                        "STRENGTH": strength
                    }
            return json.dumps(drink_dict)
        except DrinkException as e:
            self.error(e)
