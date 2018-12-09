import time
import machine
import onewire, ds18x20

class Temperature(): 
  def __init__(self):
    # the device is on GPIO12
    self.dat = machine.Pin(12)

    # create the onewire object
    self.ds = ds18x20.DS18X20(onewire.OneWire(self.dat))
    
    roms = self.ds.scan()
    if roms:
      self.rom = roms[0]
      
    print('found devices:', roms)
  
  def get_temperature(self):
    self.ds.convert_temp()
    self.temperature = self.ds.read_temp(self.rom)
    print('temperatures: ', self.temperature)
    return float("{:.2f}".format(self.temperature))




