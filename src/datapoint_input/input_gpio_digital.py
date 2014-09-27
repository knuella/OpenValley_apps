import RPi.GPIO as gpio

from input import *

class InputDPGPIOdigital(InputDP):

    def __init__(self, channel):
        InputDP.__init__(self)

        self.channel = channel
        
        gpio.cleanup()
        gpio.setmode(gpio.BOARD)
        gpio.setwarnings(False)
        gpio.setup(channel, gpio.IN)

    def read_outside_value(self):    
        try:
            self._actual_value = gpio.input(self.channel)
            self._state = 'good'
        except:
            self._state = 'bad'
            self._actual_value = 0



def main():
    dp = InputDPGPIOdigital(13)
                            
    while True:
        dp.run()


if __name__ == '__main__':
    main()

