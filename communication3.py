import time
import serial

ser = serial.Serial('/dev/ttyACM0', baudrate = 115200, timeout=1)

if ser.is_open:
    user_input = "OPEN".upper()
    ser.write(user_input.encode())
    print(f'Sent command: {user_input}')
    time.sleep(3)

