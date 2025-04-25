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

If SPI0 : 
| Signal    | GPIO (BCM) | Pin (BOARD) | Connect to MAX6675 |
|-----------|------------|-------------|---------------------|
| **CS**    | GPIO8      | 24          | CS                  |
| **SCK**   | GPIO11     | 23          | SCK                 |
| **SO**    | GPIO9      | 21          | SO                  |
| **3.3V**  | 3.3V       | 1 (or 17)   | VCC                 |
| **GND**   | GND        | 6 (or 25)   | GND                 |

> ⚠️ Only use 3.3V, **do not connect to 5V!**

---

## 🚀 Usage

### 1. Install

```bash
git clone https://github.com/your-username/max6675-temp-sensor-py.git
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

sensor = MAX6675(CS=24, SCK=23, SO=21, unit=1)  # BOARD pins

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

---

## 📄 License

MIT License
```

---

이제 `example.py`와 `max6675_sensor_lib.py` 파일을 해당 리포지토리에 추가하시면 완성됩니다.  
원하시면 `example.py` 템플릿도 바로 제공해드릴게요!

--- 

깃허브 계정에 직접 적용하거나, PR 형태로 도와드릴 수도 있어요. 어떻게 도와드릴까요?
