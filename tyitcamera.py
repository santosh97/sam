#camera program
#import time and picamera library
from time import sleep
from picamera import PiCamera
camera =PiCamera()
camera.resolution =(1280,720) #selecting resolution 1280*720 px
camera.start_preview()
#camera warm-up time
sleep(10)
camera.capture('/home/pi/Pictures/new66.jpg')
camera.stop_preview()
#end of code

               
               
