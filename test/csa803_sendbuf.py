#!/usr/bin/python3

import serial
import sys

if len(sys.argv) < 3:
    print("Usage: %s <serport> <image file>")
    sys.exit(0)

serport    = sys.argv[1]
image_file = sys.argv[2]
ser = serial.Serial(port=serport, 
                    baudrate=9600, 
                    bytesize=serial.EIGHTBITS,  # number of databits
                    parity=serial.PARITY_NONE,  # enable parity checking
                    stopbits=serial.STOPBITS_ONE,
                    rtscts=1, 
                    timeout=10) # Defaults to 8-N-1

f = open(image_file,'rb')

a=b''
while True:
    a=f.read(1)
    if a!=b'':
        ser.write(a)
        #print("%02X"%ord(a))
    else:
        break

