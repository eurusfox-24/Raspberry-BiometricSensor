# Raspberry Pi Biometric Sensor

Raspberry Pi biometric sensor (oximeter, LED display). This project reads real-time data like heart rate and oxygen levels and shows it on the screen. It tests the core technology of health sensors and microcomputers working together.

## Components Used
* Raspberry Pi
* Breadboard
* Jumper wires
* Oximeter sensor (MAX30102)
* LED display (SSD1306)

## How to Replicate

If you want to understand how this system works, the best way is to build it and test it practically. Follow these steps to set up the software and hardware on your Raspberry Pi.

### 1. Download the Code
Open your Raspberry Pi terminal and clone this repository to your local machine:
```bash
git clone [https://github.com/yourusername/pi-biometric-sensor.git](https://github.com/yourusername/pi-biometric-sensor.git)
cd pi-biometric-sensor
```

### 2. Enable I2C Communication
The Raspberry Pi needs I2C enabled to talk to the sensor and display.
* Run this command in your terminal: `sudo raspi-config`
* Navigate to **Interface Options** > **I2C**.
* Select **Yes** to enable it, then exit and reboot your Pi.

### 3. Wire the Components
Disconnect the power from your Raspberry Pi before wiring. Connect both the MAX30102 oximeter and the SSD1306 OLED display to the Pi's I2C pins using your breadboard:
* **VCC (Power):** Connect to Raspberry Pi Pin 1 (3.3V)
* **GND (Ground):** Connect to Raspberry Pi Pin 6 (GND)
* **SDA (Data):** Connect to Raspberry Pi Pin 3 (GPIO 2 / SDA)
* **SCL (Clock):** Connect to Raspberry Pi Pin 5 (GPIO 3 / SCL)

### 4. Install Required Libraries
Install the basic Python libraries needed to run the code using the included requirements file:
```bash
pip install -r requirements.txt
```

### 5. Run the System
Execute the main Python script to start the biometric readings:
```bash
python main.py
```
Once the code is running, place your finger lightly on the red light of the oximeter sensor. You will see the raw data update on the LED display in real-time.
