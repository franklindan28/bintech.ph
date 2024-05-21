import serial
import time

def establish_serial_connection(port):
    try:
        ser = serial.Serial(port, baudrate = 115200, timeout=1)
        print(f"Serial Connection established on {port}")
        return ser
    except serial.SerialException:
        print(f"Failed to establish serial connection on {port}")
        return None


def main():
    serial_ports = ['/dev/ttyACM0','/dev/ttyUSB0','/dev/ttyUSB1','/dev/ttyUSB2','/dev/ttyUSB3','/dev/ttyS0','/dev/ttyTHS1','/dev/ttyTHS2']

    for port in serial_ports:
        ser = establish_serial_connection(port)
        if ser:
            break
    if not ser:
        print("Failed to establish connection!")
        return

    try:
        while True:
            user_input = input("Enter Command (start): ").upper()
            ser.write(user_input.encode())
            print(f'Sent command: {user_input}')
            
            
    except KeyboardInterrupt:
       print("Terminated! Restart the System!")
       ser.close()
       
       

if __name__ == "__main__":
    main()