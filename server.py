import json
import time
import pdb
import RPi.GPIO as GPIO
from lib.base import BaseDrinkClass
from enum import Enum
from lib.protocol import ALCOHOL_TO_PUMP
from lib.protocol import DrinkServerSocket

def get_all_pins():
    return list(map(lambda pin: pin.value, ALCOHOL_TO_PUMP))

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(get_all_pins(), GPIO.OUT, initial=GPIO.HIGH)

class DrinkServer(BaseDrinkClass):
    def __init__(self) -> None:
        super().__init__()
        self.header = 10

    def operate_pump(self, pump, strength):
        for _ in range(1, strength):
            GPIO.output(pump, GPIO.LOW)
            time.sleep(3)
            GPIO.output(pump, GPIO.HIGH)
            time.sleep(1)

    def dispense_liquid(self, liquid, strength):
        pump_num = ALCOHOL_TO_PUMP[liquid].value
        self.operate_pump(pump_num, strength)

    def parse_recipe(self, req):
        recipe = json.loads(req)
        alcohol = recipe.get("ALCOHOL")
        mixer = recipe.get("MIXER")
        strength = recipe.get("STRENGTH")
        if alcohol == "CLEANER":
            self.info("Initializing Cleaning cycle")
            self.dispense_liquid("CLEANER", strength)
        else:
            self.debug(f"Dispensing {alcohol}")
            self.dispense_liquid(alcohol, strength)
            self.debug(f"Dispensing {mixer}")
            self.dispense_liquid(mixer, 5)
        return recipe.get("NAME")
 

    def run(self):
        server = DrinkServerSocket()
        server_sock = server.bind_and_listen()
        self.info("Server listening...")
        while True:
            clientsocket, addr = server_sock.accept()
            data = clientsocket.recv(1024)
            self.info(f"Data Recvd {data} from {addr}")
            name = self.parse_recipe(data)
            clientsocket.send(bytes(f"Dispensed {name}", "utf-8"))
if __name__ == "__main__":
    alfred = DrinkServer()
    alfred.run()
    GPIO.cleanup()