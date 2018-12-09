import time, machine
import sys, ssd1306
import numbers
from machine import I2C, Pin
from temperature import Temperature

i2c = I2C(sda=Pin(5), scl=Pin(4))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

temp = Temperature()

while True:
  display.fill(0)
  display.text('TEMPERATURA', 2, 2, 100)
  numbers = get_number(str(temp.get_temperature()) + 'ºC')
  aux_col = 1
  for number in numbers:
    aux_col += 12
    for x, row in enumerate(number):
        for y, col in enumerate(row):
            if col == "1":
                display.pixel(y+aux_col, x+20, 200)
              
  display.show()
  time.sleep_ms(1000)








