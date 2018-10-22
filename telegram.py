
import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO
from telepot.loop import MessageLoop

red=15#Posotive pin

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(red,GPIO.OUT)
GPIO.output(red,0)

message=''

def action(msg):
        chat_id = msg['chat']['id']
        cm= msg['text']
        print ('Recieved: %s'%cm)
        if 'on' in cm :
                                
                message='turn on'
        if 'red' in cm :
                message=message+'red '
                GPIO.output(red,1)
                message=message+'light(s)'
                telegram_bot.sendMessage(chat_id,message)
        if 'off' in cm :
                message='turn off '
                GPIO.output(red,0)
        if 'all' in cm:
                #message=message+'all '
                #GPIO.output(red,0)
                message=message+'light(s)'
                telegram_bot.sendMessage(chat_id,message)
telegram_bot = telepot.Bot('659256980:AAFKdWAbqMgVu-CYp_-3vaTI67Adgd_0384')

print(telegram_bot.getMe())
MessageLoop(telegram_bot,action).run_as_thread()
print('Running and Up')
while 1:
        time.sleep(10)
        

