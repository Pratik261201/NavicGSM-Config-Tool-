import serial
import time

def set_baud_rate_to_9600(port):
    # This sets COM1 to 9600 baud and saves to both SRAM and FLASH
    command = bytes([
    0xA0, 0xA1,       # Start
    0x00, 0x04,       # Payload length: 4 bytes
    0x05,             # Message ID: Configure Serial Port
    0x00,             # COM Port: COM1
    0x01,             # Baud Rate: 9600
    0x01,             # Attributes: Save to SRAM & FLASH
    0x05,             # Checksum: XOR(05 ^ 00 ^ 01 ^ 01) = 0x05
    0x0D, 0x0A        # End
])


    try:
        # Current baud rate must match what the device is using now (likely 115200)
        ser = serial.Serial(port, baudrate=115200, timeout=1)
        time.sleep(2)

        ser.write(command)
        print(f"Command sent: {command.hex().upper()}")

        # Try reading ACK/NACK
        response = ser.read(10)
        print(f"Response: {response.hex().upper()}")
        ser.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    serial_port = "COM5"  # Change to your actual port
    set_baud_rate_to_9600(serial_port)
