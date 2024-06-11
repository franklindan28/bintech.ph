import serial
import time

global ser

def establish_serial_connection(port):
    try:
        global ser
        ser = serial.Serial(port, baudrate = 115200, timeout=1)
        print(f"Serial Connection established on {port}")
        return ser
    except serial.SerialException:
        print(f"Failed to establish serial connection on {port}")
        return None


def init_serial():
    global ser
    serial_ports = ['/dev/ttyACM0','/dev/ttyUSB0','/dev/ttyUSB1','/dev/ttyUSB2','/dev/ttyUSB3','/dev/ttyS0','/dev/ttyTHS1','/dev/ttyTHS2']

    # serial_ports = ['COM1','COM2', 'COM3', 'COM4']

    for port in serial_ports:
        ser = establish_serial_connection(port)
        if ser:
            ser.open()
            break

    if not ser:
        print("Failed to establish connection!")
        return

def main(command):
    global ser
    ser.close()
    ser.open()
    command = command.upper()
    ser.write(command.encode())
    time.sleep(5)
    print(f'Sent command: {command}')
       
init_serial()
while True:
    command = input("Enter command: ")
    main(command)
