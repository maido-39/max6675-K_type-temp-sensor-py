"""
MAX6675 Thermocouple Sensor Interface for Raspberry Pi
------------------------------------------------------
This script interfaces a MAX6675 thermocouple temperature sensor using
RPi.GPIO. It initializes GPIO pins, reads temperature in Celsius, and
prints it every second.

Usage:
- Connect MAX6675 to the Raspberry Pi via SPI-like GPIO (not hardware SPI).
- Update pin numbers in the `MAX6675` class instantiation accordingly.
- Run this script directly to see temperature output every second.

Pin Definitions (BOARD numbering):
----------------------------------
> This Code, you will use PIN(BOARD) number - e.g. SPI1-{36,40,35}
+----------+--------------+------------------+------------------+
| SPI Bus  | Signal       | Pin (BOARD)      | GPIO (BCM)       |
+==========+==============+==================+==================+
| SPI0     | CS0          | 24               | GPIO8            |
|          | SCK          | 23               | GPIO11           |
|          | SO (MISO)    | 21               | GPIO9            |
+----------+--------------+------------------+------------------+
| SPI1     | CS0          | 36               | GPIO16           |
|          | SCK          | 40               | GPIO21           |
|          | SO (MISO)    | 35               | GPIO19           |
+----------+--------------+------------------+------------------+

Temperature Units:
- unit = 0: raw digital value
- unit = 1: degrees Celsius
- unit = 2: degrees Fahrenheit
"""

import RPi.GPIO as GPIO
import time

class MAX6675:
    def __init__(self, CS, SCK, SO, unit=1):
        """Initialize GPIO pins for MAX6675 communication."""
        self.cs = CS
        self.sck = SCK
        self.so = SO
        self.unit = unit  # 0: Raw, 1: Celsius, 2: Fahrenheit

        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(self.cs, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(self.sck, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.so, GPIO.IN)

    def read_temp(self):
        """Read temperature from MAX6675 and convert to the desired unit."""
        # Wake up the sensor
        GPIO.output(self.cs, GPIO.LOW)
        time.sleep(0.002)
        GPIO.output(self.cs, GPIO.HIGH)
        time.sleep(0.22)

        GPIO.output(self.cs, GPIO.LOW)

        # Discard the first null bit
        GPIO.output(self.sck, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(self.sck, GPIO.LOW)

        Value = 0
        # Read 12-bit temperature data
        for i in range(11, -1, -1):
            GPIO.output(self.sck, GPIO.HIGH)
            Value += GPIO.input(self.so) * (2 ** i)
            GPIO.output(self.sck, GPIO.LOW)

        # Read thermocouple input status (1 if not connected)
        GPIO.output(self.sck, GPIO.HIGH)
        error_tc = GPIO.input(self.so)
        GPIO.output(self.sck, GPIO.LOW)

        # Skip the remaining 2 bits
        for _ in range(2):
            GPIO.output(self.sck, GPIO.HIGH)
            time.sleep(0.001)
            GPIO.output(self.sck, GPIO.LOW)

        GPIO.output(self.cs, GPIO.HIGH)

        if error_tc != 0:
            return None  # Thermocouple not connected

        # Convert value to selected temperature unit
        if self.unit == 0:
            return Value
        elif self.unit == 1:
            return Value * 0.25
        elif self.unit == 2:
            return Value * 0.25 * 9.0 / 5.0 + 32.0

    def cleanup(self):
        """Clean up GPIO resources."""
        GPIO.cleanup()


# Run this script directly to continuously read and print temperature
if __name__ == "__main__":
    try:
        # Replace pin numbers with your actual connections
        sensor = MAX6675(CS=36, SCK=40, SO=35, unit=1)  # Celsius output

        while True:
            temp = sensor.read_temp()
            if temp is not None:
                print(f"Temperature: {temp:.2f} °C")
            else:
                print("Sensor error or not connected.")
            time.sleep(1)

    except KeyboardInterrupt:
        print("Stopped by user.")

    finally:
        sensor.cleanup()
