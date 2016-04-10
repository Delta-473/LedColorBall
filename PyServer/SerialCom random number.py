import sys
import time
import serial
import asyncio
import random
import ledbol

print ("Python Serial Ledbol Random Number Server Terminal V0.1\n")

'''#open config file
#TODO: Add exception when config is missing cannot be opend.
config = open("config.txt","r")

COM = config.readline()
COM = COM.replace("SERIALPORT: ","",1)
COM = COM.rstrip('\n')  #stripping newline charachter

BAUD = config.readline()
BAUD = BAUD.replace("BAUDRATE: ","",1)
BAUD = BAUD.rstrip('\n')

print("DEBUG: opening config file succesfull\n")

# configure the serial connection
ser = serial.Serial(
    port = COM,
    baudrate = BAUD,
    parity = serial.PARITY_NONE,    #uitlezen vanuit configbestand werkt nog niet
    stopbits = serial.STOPBITS_ONE, #geeft error vb: serial.PARITY module serial
    bytesize = serial.EIGHTBITS     #has no attribute 'PARITY'
)

ser.isOpen()
'''
print ("Enter your commands below. \r\nInsert exit to leave the application.")

R = 0
G = 0
B = 0

global rood
global groen
global blauw
        
while 1 :
    
    rood = ledbol.randomColor()
    groen = ledbol.randomColor()
    blauw = ledbol.randomColor()
    
    rood = rood.encode('ascii','replace')
    groen = groen.encode('ascii','replace')
    blauw = blauw.encode('ascii','replace')
    print(rood)
    print(groen)
    print(blauw)
    
    ledbol.sendLed(rood,groen,blauw)
    #time.sleep(5)
