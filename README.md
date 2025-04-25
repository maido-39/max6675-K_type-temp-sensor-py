# max6675-temp-sensor-py

🧪 Python module for reading MAX6675 thermocouple sensor data using Raspberry Pi GPIO (bit-banged SPI)

---

## 🔧 Features

- Read temperature from MAX6675 using GPIO
- Celsius, Fahrenheit, or raw output
- Uses bit-banged SPI (no hardware SPI required)
- Simple class interface

---

## 📷 Wiring (Raspberry Pi 4)
```
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
```

---

## 🚀 Usage

### 1. Install

```bash
git clone https://github.com/maido-39/max6675-temp-sensor-py.git
cd max6675-temp-sensor-py
```

### 2. Run example

```bash
python3 example.py
```

---

## 🧩 Library Example

```python
from max6675_sensor_lib import MAX6675
import time

sensor = MAX6675(CS=35, SCK=40, SO=36, unit=1)  # BOARD pins

while True:
    temp = sensor.read_temp()
    print(f"Temperature: {temp:.2f} °C")
    time.sleep(1)
```

---

## 📁 Files

- `max6675_sensor_lib.py`: Main library
- `example.py`: Basic test script
- `README.md`: Docs
