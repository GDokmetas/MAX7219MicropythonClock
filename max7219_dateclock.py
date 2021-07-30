# Connections:
# SCK (CLK) -> GPIO4
# MOSI (DIN) -> GPIO2
# SS (CS) -> GPIO5

from machine import Pin, SPI, UART
import max7219_8digit
import time

spi = SPI(1, baudrate=100000, polarity=1, phase=0, sck=Pin(10), mosi=Pin(11))
ss = Pin(12, Pin.OUT)
uart = UART(1, 9600, tx = Pin(8), rx = Pin(9))
display = max7219_8digit.Display(spi, ss)
display.write_to_buffer("        ")
display.display()
display.set_register(0x0a, 2)

while True:
    s = uart.read(8)
    s = s.decode('utf-8')
    if ( s != ""):
        display.write_to_buffer(s)
        display.display()
        