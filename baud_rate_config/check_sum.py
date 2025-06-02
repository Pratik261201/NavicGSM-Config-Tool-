payload = [0x05, 0x00, 0x01, 0x01]
checksum = 0
for byte in payload:
    checksum ^= byte
print(f"Checksum: {checksum:#04x}")  # Outputs: 0x05
