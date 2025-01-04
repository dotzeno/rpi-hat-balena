import time
import os
import subprocess
import busio
import smbus
bus = smbus.SMBus(1)
time.sleep(1)

hat_addr = 0x0d
fan_reg = 0x08
rgb_off_reg = 0x07
Max_LED = 3

def setRGB(num, r, g, b):
    bus.write_byte_data(hat_addr, 0x00, num&0xff)
    bus.write_byte_data(hat_addr, 0x01, r&0xff)
    bus.write_byte_data(hat_addr, 0x02, g&0xff)
    bus.write_byte_data(hat_addr, 0x03, b&0xff)

bus.write_byte_data(hat_addr, rgb_off_reg, 0x00)
setRGB(Max_LED, 0, 0, 0)