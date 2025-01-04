import time
import os
import subprocess
import busio
import smbus
bus = smbus.SMBus(1)
time.sleep(1)
hat_addr = 0x0d
fan_reg = 0x08
g_temp=0

def setFanSpeed(speed):
    bus.write_byte_data(hat_addr, fan_reg, speed&0xff)

def getTemp():
    cmd = os.popen('cat /sys/class/thermal/thermal_zone*/temp').readline().strip()
    g_temp = int(cmd[:2])
    print("Temp:",g_temp)

while True:
    time.sleep(1)
    getTemp()
    if g_temp >= 45:
        setFanSpeed(0x01)
    elif g_temp >= 47:
        setFanSpeed(0x02)
    elif g_temp >= 49:
        setFanSpeed(0x03)
    elif g_temp >= 51:
        setFanSpeed(0x04)
    elif g_temp >= 53:
        setFanSpeed(0x05)
    elif g_temp >= 55:
        setFanSpeed(0x06)
    elif g_temp >= 57:
        setFanSpeed(0x07)
    elif g_temp >= 59:
        setFanSpeed(0x08)
    elif g_temp >= 61:
        setFanSpeed(0x09)
    else:
        setFanSpeed(0x00)
    time.sleep(1)