import time
import board
import busio
import adafruit_ssd1306
import adafruit_max30102

# Set up the basic I2C communication
i2c = busio.I2C(board.SCL, board.SDA)

# Set up the LED Display (128x32 resolution)
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# Set up the Oximeter sensor
sensor = adafruit_max30102.MAX30102(i2c)

# Create a continuous loop to read and display data
while True:
    # Read the raw red and infrared data from the sensor
    red_reading, ir_reading = sensor.read_sequential()
    
    # Clear the previous data from the display
    display.fill(0)
    
    # Write the new text and data to the display
    display.text("Biometric Data:", 0, 0, 1)
    display.text(f"Red: {red_reading[0]}", 0, 10, 1)
    display.text(f"IR: {ir_reading[0]}", 0, 20, 1)
    
    # Turn on the pixels to show the text
    display.show()
    
    # Wait half a second before taking the next reading
    time.sleep(0.5)
