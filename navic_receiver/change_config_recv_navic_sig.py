import serial
import time

def set_navic_constellation_only(port):
    # Command to configure GNSS constellation type to NavIC only
    command = bytes([
        0xA0, 0xA1,       # Start bytes
        0x00, 0x05,       # Payload length: 5 bytes
        0x64,             # Message ID
        0x19,             # Sub ID
        0x00,             # Constellation byte 1 (MSB)
        0x10,             # Constellation byte 2 (LSB) -> Bit 4 set for NavIC only
        0x00,             # Attributes: 0 (update to SRAM only)
        0x6D,             # Checksum (XOR of payload bytes)
        0x0D, 0x0A        # End bytes
    ])

    try:
        # Open serial port at current baud rate (adjust if needed)
        ser = serial.Serial(port, baudrate=9600, timeout=2)
        time.sleep(2)  # Wait for serial port to settle

        ser.write(command)
        print(f"Command sent: {command.hex().upper()}")

        # Read response (ACK/NACK or other)
        response = ser.read(10)
        print(f"Response: {response.hex().upper()}")

        ser.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    serial_port = "COM5"  # Change to your actual port
    set_navic_constellation_only(serial_port)
