__author__ = 'sachinpatney'

import serial
import time

ser = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1.0)

s = b''

while True:
        bytesToRead = ser.inWaiting()

        if bytesToRead > 0:
            s += ser.read(bytesToRead)
        else:
            if len(s) > 0:
                print(s)
            s = b''
            time.sleep(1)