import sys
import gnublin

sys.path.append("../../base/src")
from rpisps.exceprions import *
from output import *

class OutputDPGnublinRelay(OutputDP):

    def __init__(self, safety_value, module_address, clamp_address):
        super().__init__(safety_value)
        
        self.modul = gnublin.gnublin_module_relay()
        self.modul.setAddress(modul_address)
        if clamp_address >= 1 and clamp_address <= 4:
            self.clamp_address = clamp_address
        else:
            raise InputError("relayAddress should be between 1 and 4.")

    def write_outside_value(self):    
        if self.modul.switchPin(self.clamp_address, to_set_value) != -1:
            self._good = True
        else:
            self._good = False


def main():
    dp = OutputDPGnublinRelay(1)
    while True:
        dp.run()


if __name__ == '__main__':
    main()

