import serial
import time

# Pyserial Docs: https://pyserial.readthedocs.io/en/latest/shortintro.html

# You may configure the HC-12 433MHz transceiver using the datasheet below
# https://statics3.seeedstudio.com/assets/file/bazaar/product/HC-12_english_datasheets.pdf

# Connects to a 433MHz joined to a UART USB Bridge at COM8 (for example)
# This 433MHz transceiver is in-charge of sending signals out
# Check using Device Manager which is the COM port
ser = serial.Serial('COM3')
ser.baudrate = 9600 # Baud Rate configured in the HC-12, refer to datasheet to set
ser.timeout = None

# ser_bytes = ser.readline()
# print(ser_bytes)
while True:
    if (command := input()):
        ser.write(str.encode(command + '\n', "utf-8"))
        print("Sent!")
        time.sleep(1)
