import serial
import time

class SerialComm:
    """
    A class to handle serial communication.
    Attributes:
    -----------
    ser : serial.Serial
        The serial port object.
    command_map : dict
        A dictionary mapping commands to their corresponding methods.
    Methods:
    --------
    __init__(port='COM4', baudrate=9600, timeout=1):
        Initializes the serial port with the given parameters.
    do_ping():
        Returns a 'pong' response for a 'ping' command.
    default():
        Returns a default response when an unknown command is received.
    read_command():
        Reads a command from the serial port.
    execute_command(command):
        Executes the given command by looking it up in the command_map.
    run():
        Continuously reads and executes commands from the serial port.
    """
    def __init__(self, port='COM4', baudrate=9600, timeout=1):
        try:
            self.ser = serial.Serial(port, baudrate, timeout=timeout)
        except serial.SerialException as e:
            print(f"Error initializing serial port: {e}")
            self.ser = None
        self.command_map = {
            b'ping': self.do_ping,
        }

    def do_ping(self):
        return b'pong'

    def default(self):
        return b'meow'

    def read_command(self):
        command = self.ser.readline().strip()
        return command

    def execute_command(self, command):
        if command in self.command_map:
            response = self.command_map[command]()
        else:
            response = self.default()
        print(response)
        self.ser.write(response)

    def run(self):
        while True:
            command = self.read_command()
            if command:
                print(command)
                self.execute_command(command)
            time.sleep(1)

if __name__ == "__main__":
    serial_comm = SerialComm()
    serial_comm.run()