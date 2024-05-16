import serial
import time

# Define Arduino serial port
arduino_port = 'COM3'  # This might vary depending on your setup
baud_rate = 9600

# Define RFID card UIDs
authorized_uid =""

# Open serial connection to Arduino
try:
    arduino = serial.Serial(arduino_port, baud_rate)
    print("Arduino connected successfully.")
except serial.SerialException as e:
    print(f"Failed to connect to Arduino: {e}")
    exit()

# Main loop
while True:
    # Read data from Arduino
    arduino_data = arduino.readline().decode().strip()
    print("Result: ",arduino_data)
    
    # Check if data is available
    if arduino_data:
        print("Received UID:", arduino_data)
        
        # Check if received UID matches authorized UID
        if arduino_data == authorized_uid:
            print("Authorized access", authorized_uid)
            # Send a message back to Arduino to turn on the green LED
            arduino.write(b'1\n')
        elif arduino_data != authorized_uid:
            print("Access denied")
            # Send a message back to Arduino to turn on the red LED
            arduino.write(b'0\n')
    
    # Delay before checking again
    time.sleep(1)

# Close serial connection
arduino.close()
