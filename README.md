# NavicGSM-Config-Tool

Tools and scripts to configure Navic GSM / GNSS module parameters such as baud rate, serial port settings, and more.

## Structure

- `baud_rate_config/`: Scripts to change and test baud rates.
- `parameter_config/`: Scripts to change and test other module parameters.
- `utils/`: Helper functions for serial communication and checksums.
- `docs/`: Documentation about commands and usage.

# How to Use This Repository

Follow these steps to get started:

## 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>

2. Create and Activate a Virtual Environment
Create a new virtual environment named GPS:
```bash
python -m venv GPS

Activate the virtual environment:

Windows (PowerShell or Command Prompt):

```bash
GPS\Scripts\activate

macOS / Linux:

```bash
source GPS/bin/activate

3. Navigate to the baud_rate_config Subfolder
```bash
cd baud_rate_config
Inside this folder, you’ll find a separate README.md that describes the specific project details for changing the GPS baud rate. Be sure to review that file for project-specific instructions.

4. Install Dependencies:

Within the baud_rate_config directory (or any other subfolder with its own requirements.txt), run:
```bash
pip install -r requirements.txt

5. Run Scripts Inside Subfolders
Each subfolder contains Python scripts relevant to its functionality. For example, in baud_rate_config you might see scripts like:

change_baudrate.py
check_sum.py
read_gps.py

To execute a script, simply run:
```bash
python <script_name>.py
Example:
```bash
python change_baudrate.py

Notes:

Always verify your COM port and current baud rate before running any script.

The Attributes field in the command packet determines whether the change is saved persistently (1) or temporarily (0).

Use the check_sum.py script to calculate the checksum whenever you modify payloads.

Ensure no other program is using the COM port during the operation (e.g., Arduino Serial Monitor, PuTTY).


