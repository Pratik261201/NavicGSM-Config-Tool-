Great! Here's a **complete `README.md`** file for your `navic_receiver` folder that documents your Python code for receiving and identifying NavIC signals from a GNSS module.

---

### ✅ `navic_receiver/README.md`

````markdown
# 📡 NavIC Signal Receiver (Python)

This module provides a Python-based solution to read and process NavIC (IRNSS) satellite signals using a GNSS module that supports `$PIRNSF`, `$GNGGA`, `$GNGLL`, `$GNRMC`, and `$GIGSV` NMEA sentences.

---

## 📁 Folder Contents

| File | Description |
|------|-------------|
| `navic_receive.py` | Python script for real-time serial data reading from GNSS module. |
| `README.md`        | Guide to set up and use the NavIC receiver script. |
| `NavIC_Reference_Doc.pdf` | Reference document explaining NMEA sentences and NavIC satellite details. |

---

## ⚙️ Requirements

- A GNSS module that supports IRNSS (NavIC), such as u-blox M9N, Quectel L76K, or equivalent.
- USB to serial cable (or UART connection to Raspberry Pi/ESP32).
- Python 3.7+
- Libraries:
  ```bash
  pip install pyserial
````

---

## 🚀 Usage Instructions

1. **Connect your GNSS module** to your PC via USB or serial UART.
2. **Edit serial port settings** in `navic_receive.py`:

   ```python
   SERIAL_PORT = "COM3"     # Windows: COMx, Linux: /dev/ttyUSBx or /dev/ttySx
   BAUD_RATE = 9600         # Usually 9600 or 115200 depending on your module
   ```
3. **Run the script**:

   ```bash
   python navic_receive.py
  
4. The terminal will output real-time NMEA sentences.

   * Look for `$PIRNSF` or `$GIGSV` entries indicating active NavIC satellites.

---

## 🔍 How to Identify NavIC Signals

* NavIC (IRNSS) satellites are typically shown in NMEA `$GIGSV` or `$PIRNSF` sentences.
* Satellite IDs specific to NavIC usually fall in the PRN range: **R01 to R09**.
* Example line:

  ```bash
  $PIRNSF,10,4,8B,1F,70,...
  

---

## 📄 Customize the Script

You can modify `navic_receive.py` to:

* Log data to a CSV or text file.
* Filter only NavIC-related sentences.
* Send data to a dashboard or web server.

---

## 🛰️ Tested Setup

| Component   | Details                                     |
| ----------- | ------------------------------------------- |
| GNSS Module | SkyTra P1125S-01A                           |
| OS          | Windows 11                                  |
| Interface   |  UART                                       |
| Tools       | Python 3.10, GNSS Viewer (for confirmation) |

---

## 🧠 Reference

See `NavIC_Reference_Doc.pdf` for:

* Detailed explanation of `$PIRNSF`, `$GNGGA`, `$GNRMC`, etc.
* Satellite ID mapping for PIRNSS [Proprietary Indian Regional Navigation Satellite System] also Known as NavIC.
* Sentence structures and expected outputs.

---

## 🤝 Contributing

Feel free to submit pull requests or suggest improvements to support more GNSS modules and enhance compatibility.

---

## 🛡️ License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

## 👨‍💻 Author

**Pratik Chouragadey**

```


