import RPi.GPIO as GPIO
import time
import serial

def read_rfid ():
    ser=serial.Serial("/dev/ttyUSB0")
    ser.baudrate = 9600
    data=ser.read(12)
    ser.close()
    return data
try:

    while(True):
        id=read_rfid ()
        print(id)
        if id==b'1C003917E9DB':
            print("Access Granted")

        else:
            print("Access Denied")

finally:
    GPIO.cleanup()
