import serial
import time

ser = serial.Serial('COM7', 9600)

def On_Off(con):
    return con

while True:
    if ser.readable():
        # val = input()

        val = On_Off('1')

        if val == '1':
            val = val.encode('utf-8')
            ser.write(val)
            print("LED TURNED ON")
            time.sleep(0.5)

        elif val == '0':
            val = val.encode('utf-8')
            ser.write(val)
            print("LED TURNED OFF")
            time.sleep(0.5)
