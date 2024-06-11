import time
import serial

ser = serial.Serial('/dev/ttyACM0', baudrate = 115200, timeout=1)

#while True:
def send_command(user_input):
    # user_input = input("Enter Command: ").upper()
    user_input = user_input.upper()
    print("user_input_encode: ", user_input.encode())
    ser.write(user_input.encode())
    ser.flush()
    time.sleep(0.1)
    print(f'Sent command: {user_input}')

time.sleep(5)
send_command("OPEN")
time.sleep(5)
send_command("CLOSE")
time.sleep(5)
send_command("PET")

