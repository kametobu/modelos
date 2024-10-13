from time import sleep
import serial

ser = serial.Serial("COM3", 9600)
while True:
    sleep(1)
    getVal = ser.readline()
    print(getVal)
