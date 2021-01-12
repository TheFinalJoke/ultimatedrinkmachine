import json
import RPi.GPIO as GPIO
from lib.base import BaseDrinkClass
from enum import Enum
from lib.protocol import Alcohol_to_Pump
from lib.protocol import DrinkServerSocket

import pdb

class PinToPump(Enum):
    pass

class DrinkServer(BaseDrinkClass):
    def __init__(self) -> None:
        super().__init__()
        self.header = 10

    def operate_pump(self, pump, strength=None):
        pass

    def dispense_alcohol(self, alcohol, strength):
        pump_num = Alcohol_to_Pump[alcohol].value
        self.operate_pump(pump_num, strength)

    def parse_recipe(self, req):
        recipe = json.loads(req)
        alcohol = recipe.get("ALCOHOL")
        mixer = recipe.get("MIXER")
        strength = recipe.get("STRENGTH")

        
        
    def run(self):
        server = DrinkServerSocket()
        server_sock = server.bind_and_listen()
        self.info("Server listening...")
        while True:
            clientsocket, addr = server_sock.accept()
            data = clientsocket.recv(1024)
            self.info(f"Data Recvd {data}")
            clientsocket.send(bytes(f"Data Accepted from {addr}", "utf-8"))
            self.parse_recipe(data)
if __name__ == "__main__":
    alfred = DrinkServer()
    alfred.run()