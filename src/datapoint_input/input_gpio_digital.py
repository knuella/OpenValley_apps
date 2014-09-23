import RPi.GPIO as gpio

from input import *

class InputDPGPIOdigital(InputDP):

    def __init__(self, channel):
        InputDP.__init__(self)
        
        gpio.setmode(gpio.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(channel, GPIO.IN)

    def read_outside_value(self):    
        try:
            GPIO.input(channel)
            self._state = 'good'
        except:
            self._state = 'bad'


def main():
    dp = InputDPGPIOdigital(13)
                            
    while True:
        dp.run()


if __name__ == '__main__':
    main()

