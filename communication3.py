import time
import serial

ser = serial.Serial('/dev/ttyACM0', baudrate = 115200, timeout=1)

if ser.is_open:
    ser.write("OPEN".encode())

