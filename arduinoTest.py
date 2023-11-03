import serial
import time

ser = serial.Serial('COM5', 9600)

while True:
    ser.write(b'1')
    time.sleep(0.1)
    response = ser.readline().decode('utf-8').strip()
    print(response)
