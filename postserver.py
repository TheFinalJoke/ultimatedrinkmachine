import RPi.GPIO as GPIO
from lib.base import BaseDrinkClass
from server import get_all_pins

class Cleanup(BaseDrinkClass):

    def __init__(self) -> None:
        super().__init__()
    
    def run_cleanup(self):
        self.info("Cleaning up GPIO Ports")
        GPIO.setup(get_all_pins(), GPIO.OUT, initial=GPIO.LOW)
        GPIO.cleanup()
    
if __name__ == "__main__":
    Cleanup().run_cleanup()
