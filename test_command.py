import serial
import time

# Pyserial Docs: https://pyserial.readthedocs.io/en/latest/shortintro.html

# You may configure the HC-12 433MHz transceiver using the datasheet below
# https://statics3.seeedstudio.com/assets/file/bazaar/product/HC-12_english_datasheets.pdf

# Connects to a 433MHz joined to a UART USB Bridge at COM8 (for example)
ser = serial.Serial('COM6')
ser.baudrate = 9600 # Baud Rate configured in the HC-12, refer to datasheet to set
ser.timeout = 1 # timeout to prevent readline from blocking

time.sleep(1) # wait for HC12 to initialize
print(ser.readline().decode("utf-8").strip() + '\n') # print AT command message

while True:
    print("--------------------") # border to make things look nicer
    command = input("Enter Command: ")
    if command == "exit":
        break
    
    
    ser.write(str.encode(command + '\n', "utf-8")) # write encoded command to serial
    while line := ser.readline().decode("utf-8").strip(): # check if line is empty
        print(line)
