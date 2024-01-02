import serial
import csv
import time

# Configuration for Arduino connection
arduino_port = "COM8"  # Specify the port where Arduino is connected
baud_rate = 9600  # Baud rate for serial communication
ser = serial.Serial(arduino_port, baud_rate, timeout=1)  # Open serial connection

# CSV file setup for storing battery data
csv_file = "battery_data.csv"  # Specify the name of the CSV file

# Continuously request and store battery voltage
while True:
    try:
        # Request battery voltage from Arduino
        ser.write(b"get_voltage\n")  # Send command to Arduino to get voltage
        response = ser.readline().decode().strip()  # Read and decode the response

        # Store data in CSV file with timestamp
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")  # Get current timestamp
        with open(csv_file, "a", newline="") as file:  # Open CSV file for writing
            writer = csv.writer(file)  # Create a CSV writer
            writer.writerow([timestamp, response])  # Write timestamp and voltage to CSV

        # Print received data and timestamp for monitoring
        print(f"Received: {response} at {timestamp}")

        # Adjust the delay as needed to control the sampling rate
        time.sleep(10)

    # Handle keyboard interrupt to gracefully exit the program
    except KeyboardInterrupt:
        print("Program terminated by user.")
        break

# Close the serial connection when the program exits
ser.close()
