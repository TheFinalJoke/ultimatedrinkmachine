import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
gpio_list = [29, 11, 13, 15, 8, 36, 38, 40]
GPIO.setup(gpio_list, GPIO.OUT, initial=GPIO.LOW)

try:
    while True:
        for chan in gpio_list:
            GPIO.output(chan, GPIO.HIGH)
            time.sleep(.1)
        for chan in gpio_list:
            GPIO.output(chan, GPIO.LOW)
            time.sleep(.1)
        time.sleep(.1)

except KeyboardInterrupt:
    GPIO.cleanup()
