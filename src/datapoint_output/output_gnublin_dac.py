import gnublin

from output import *
from scaler_linear import *

class OutputDPGnublinDAC(OutputDP):

    def __init__(self, safety_value, clamp_address, scaling_type, scaling_data):
        OutputDP.__init__(self, safety_value)
        
        self.modul = gnublin.gnublin_module_dac()
        #self.modul.setAddress(module_address)
        
        if clamp_address >= 1 and clamp_address <= 4:
            self.clamp_address = clamp_address - 1
        else:
            raise InputError("relayAddress should be between 1 and 4.")
        
        self.scaler = getattr(sys.modules[__name__],
                               scaling_type)(**scaling_data)

    def write_outside_value(self):    
        computal_value = self.scaler.get_y(_actual_value.get_value())
        
        self.modul.write(self.clamp_address, (int)(computal_value))
        
        readed_computal_value = self._modul.read(self.clamp_address)
        if computal_value == readed_computal_value:
            self._state = 'good'
        else:
            self._state = 'no connection'


def main():
    dp = OutputDPGnublinDAC(0, 1, 
                            'linearScaler', {'y1':0,'x1':2900,'y2':0,'x2':10,})
    while True:
        dp.run()


if __name__ == '__main__':
    main()

