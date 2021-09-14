import serial
import time

for i in range(10):
    with serial.Serial('COM7', 9600, timeout=1) as ser:
        time.sleep(1)
        ser.write(b'0')
        time.sleep(1)
        ser.write(b'1')
