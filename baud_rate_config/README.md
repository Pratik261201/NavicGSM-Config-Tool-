# Skytraq PX1125S GPS Module Baud Rate Changer

This project allows you to change the baud rate of the Skytraq PX1125S GPS module via serial communication using Python.

---

## Overview

The Skytraq PX1125S GPS module communicates via a serial port (COM port) with a default baud rate (usually 115200). This script sends a command packet to the module to change its baud rate to one of the supported rates (e.g., 9600). The command packet must be carefully constructed with the correct message structure and checksum.

---

## Steps to Use

### 1. Identify COM Port and Current Baud Rate

- Connect your GPS module properly to your computer.  
- Identify the correct COM port (e.g., `COM5`) assigned to your device.  
- Confirm the current baud rate of the GPS module (default is often **115200**).

---

### 2. Understand the Command Packet Structure

The packet to change baud rate consists of:

| Field Name | Example (hex) | Description                                | Type  | Unit |
|------------|---------------|--------------------------------------------|-------|------|
| Message ID | 05            | Command ID for "Configure Serial Port"     | UINT8 |      |
| COM Port   | 00            | 00 = COM1                                  | UINT8 |      |
| Baud Rate  | 01            | 0=4800, 1=9600, 2=19200, 3=38400, etc.     | UINT8 |      |
| Attributes | 01            | 0=update SRAM only, 1=update SRAM & FLASH  | UINT8 |      |

- **Payload length** for this command is 4 bytes.  
- The complete packet includes header, payload, checksum, and tail bytes.

---

### 3. Generate Checksum

The checksum is calculated by XORing all bytes in the payload (Message ID, COM port, Baud Rate, Attributes).

Example payload:

05 00 01 01


You can use the provided `check_sum.py` script to dynamically generate the checksum for any payload.

---

### 4. Integrate Checksum into Python Script

After generating the checksum, insert it into the command packet in your main Python script that sends the command to the GPS module.

Example command packet (hex):A0 A1 00 04 05 00 01 01 05 0D 0A


- `A0 A1` — Header  
- `00 04` — Payload length (4 bytes)  
- `05 00 01 01` — Payload (Message ID, COM Port, Baud Rate, Attributes)  
- `05` — Checksum  
- `0D 0A` — Tail  

---

### 5. Run the Python Script

Use the script to send the command packet over the serial port at the **current baud rate** (e.g., 115200).

```bash
python change_baudrate.py

After sending, close and reopen your serial connection at the new baud rate (e.g., 9600) to continue communication with the GPS module.

Payload Baud Rate Table

| Baud Rate Code | Baud Rate (bps) |
| -------------- | --------------- |
| 0              | 4800            |
| 1              | 9600            |
| 2              | 19200           |
| 3              | 38400           |
| 4              | 57600           |
| 5              | 115200          |
| 6              | 230400          |
| 7              | 460800          |
| 8              | 921600          |

## Notes

- Always verify your COM port and current baud rate before running the script.  
- The `Attributes` field determines whether the change is saved persistently (`1`) or temporarily (`0`).  
- Use the `check_sum.py` script to calculate the checksum when modifying payloads.  
- Ensure no other program is using the COM port during the operation.


