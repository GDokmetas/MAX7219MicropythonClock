# Connections:
# SCK (CLK) -> GPIO4
# MOSI (DIN) -> GPIO2
# SS (CS) -> GPIO5

from machine import Pin, SPI
import max7219_8digit
import time

spi = SPI(1, baudrate=100000, polarity=1, phase=0, sck=Pin(10), mosi=Pin(11))
ss = Pin(12, Pin.OUT)

display = max7219_8digit.Display(spi, ss)

display.display()
display.set_register(0x0a, 2)
sayac = 0
while True:
    s = str(sayac)
    s = (' '*(8 - len(s))+s)
    display.write_to_buffer(s)
    sayac += 1
    time.sleep(0.1)
    display.display()
        