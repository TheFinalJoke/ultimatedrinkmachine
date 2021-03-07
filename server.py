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
        self.debug(f'Operating pump {pump} for {strength} secs')
        GPIO.output(pump, GPIO.LOW)
        time.sleep(strength)
        GPIO.output(pump, GPIO.HIGH)

    def dispense_liquid(self, liquid, strength):
        pump_num = ALCOHOL_TO_PUMP[liquid].value
        self.operate_pump(pump_num, strength)
    
    def calculate_mixer_length(self, alcochol_strength):
        total_time = 180
        return total_time - alcochol_strength

    def intiate_cleancycle(self):
        try:
            pump_num = ALCOHOL_TO_PUMP['Cleaner'].value
            self.operate_pump(pump_num, 3)
        except Exception as E:
            self.error('Cleaner does not have a pump')

    def parse_recipe(self, req):
        recipe = json.loads(req)
        alcohol = recipe.get("ALCOHOL")
        mixer = recipe.get("MIXER")
        strength = recipe.get("STRENGTH")
        mixer_strength = self.calculate_mixer_length(strength)
        if alcohol == "Cleaner":
            self.info("Initializing Cleaning cycle")
            self.intiate_cleancycle()
            self.info("Finished Cleaning Cycle")
        else:
            self.debug(f"Dispensing {alcohol}")
            self.dispense_liquid(alcohol, strength)
            self.debug(f"Dispensing {mixer}")
            self.dispense_liquid(mixer, mixer_strength)
            self.debug(f"Dispensed {recipe['NAME']}")
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