
---

### ✅ Updated `README.md` for `NavicGSM-Config-Tool`

````markdown
# 🛰️ NavicGSM-Config-Tool

Tools and scripts to configure NavIC GSM / GNSS module parameters such as baud rate, satellite filtering, and real-time signal monitoring.

---

## 📁 Project Structure

| Folder | Purpose |
|--------|---------|
| `baud_rate_config/` | Scripts to change and test baud rates of supported GPS/GNSS modules. |
| `parameter_config/` | Scripts to modify other module parameters (like NMEA sentence selection, update rate, etc.). |
| `utils/` | Utility functions for serial communication, checksum calculation, and packet construction. |
| `docs/` | Technical documentation on command formats, serial protocols, and module reference sheets. |
| `navic_receiver/` | **New!** A self-contained project to receive and identify NavIC satellite signals using Python. Useful for validating NavIC support on your GNSS module.

---

## ⚙️ How to Use This Repository

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>
````

---

### 2. Create and Activate a Virtual Environment

```bash
python -m venv GPS
```

Activate the environment:

* **Windows:**

  ```bash
  GPS\Scripts\activate
  ```

* **macOS / Linux:**

  ```bash
  source GPS/bin/activate
  ```

---

### 3. Navigate to a Subfolder Based on Your Task

* To **change the GPS module baud rate**, go to:

  ```bash
  cd baud_rate_config
  ```

* To **receive and parse NavIC satellite signals**, go to:

  ```bash
  cd navic_receiver
  ```

Each folder contains its own `README.md` file that details the specific project usage and script instructions.

---

### 4. Install Required Dependencies

From within any subfolder (e.g., `baud_rate_config`, `navic_receiver`) with a `requirements.txt` file, install dependencies:

```bash
pip install -r requirements.txt
```

---

### 5. Run the Scripts

Example from `baud_rate_config/`:

```bash
python change_baudrate.py
```

Example from `navic_receiver/`:

```bash
python navic_receive.py
```

---

## 📌 Notes

* Always verify your COM port and baud rate before executing any script.
* The **Attributes field** in the GPS packet structure determines whether parameter changes are **temporary (0)** or **persistent (1)**.
* Use `check_sum.py` (in `utils/`) to validate checksum values if you modify command payloads manually.
* Ensure no other program (e.g., Arduino Serial Monitor, PuTTY) is using the serial port while running your scripts.

---

## 🛰️ Project Highlights

1. **Baud Rate Configuration Tool**
   Easily reconfigure the GNSS module's baud rate using standard protocol commands (e.g., `$PMTK`, `$PUBX`, `$CFG` depending on vendor).

2. **NavIC Signal Receiver (New!)**
   Real-time terminal-based system to identify NavIC satellites from live NMEA data.
   Check `navic_receiver/README.md` for setup and use instructions.

---

## 🧠 License

This repository is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

## 👨‍💻 Maintainer

**Pratik Chouragadey**

```


