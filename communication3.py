import serial
import time

# Configure the serial connection
ser = serial.Serial(
    port='/dev/ttyACM0',      # Replace with your port name
    baudrate=115200,    # Replace with your baudrate
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1         # Timeout in seconds
)

# Function to send a command
def send_command(command):
    if ser.is_open:
        ser.write(command)
        ser.flush()
        time.sleep(0.1)  # Small delay to ensure command is processed
    else:
        print("Serial port is not open.")

send_command(b'OPEN\r\n')
time.sleep(5)
send_command(b'CLOSE\r\n')
time.sleep(5)
send_command(b'PET\r\n')
time.sleep(5)

# Close the serial connection
ser.close()