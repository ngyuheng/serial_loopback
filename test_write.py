import serial
import time

import serial
import time

def main():
    # Configure the serial port
    try:
        ser = serial.Serial('COM6', baudrate=9600, timeout=None)
        print("Serial connection established. Type 'exit' to quit.")
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        return

    while True:
        try:
            # Prompt user for hex input
            hex_input = input("Enter Hex Values (comma-separated, e.g., '2A,00,00,00'): ").strip()
            
            if hex_input.lower() == 'exit':  # Allow the user to exit the loop
                print("Exiting...")
                break
            
            try:
                # Convert the hex string into raw bytes
                hex_values = hex_input.split(", ")
                byte_data = bytes(int(h, 16) for h in hex_values)
                # add a newline character to the end of the byte data
                byte_data += b'\r\n'
            except ValueError:
                print("Invalid hex input! Ensure values are valid hex codes separated by commas.")
                continue
            
            # Send the binary data over serial
            ser.write(byte_data)
            print(f"Sent {len(byte_data)} bytes: {byte_data}")
            
            time.sleep(1)  # Adjust delay if needed
            
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"Error: {e}")
    
    # Clean up
    ser.close()
    print("Serial connection closed.")

if __name__ == "__main__":
    main()
