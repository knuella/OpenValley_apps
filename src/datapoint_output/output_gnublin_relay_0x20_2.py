import gnublin

from output import *

class OutputDPGnublinRelay(OutputDP):

    def __init__(self, safety_value, module_address, clamp_address):
        OutputDP.__init__(self, safety_value)
        
        self.modul = gnublin.gnublin_module_relay()
        self.modul.setAddress(module_address)
        if clamp_address >= 1 and clamp_address <= 4:
            self.clamp_address = clamp_address
        else:
            raise InputError("relayAddress should be between 1 and 4.")

    def write_outside_value(self):    
        value = self._actual_value.get_value()
        if self.modul.switchPin(self.clamp_address, value) != -1:
            self._state = 'good'
        else:
            self._state = 'no connection'


def main():
    dp = OutputDPGnublinRelay(1, 0x20, 2)
    while True:
        dp.run()


if __name__ == '__main__':
    main()

