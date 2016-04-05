import sys
import time
import serial
import asyncio
import random

print ("Python Serial Ledbol Random Number Server Terminal V0.1\n")

#open config file
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

print ("Enter your commands below. \r\nInsert exit to leave the application.")

R = 0
G = 0
B = 0

global rood
global groen
global blauw

#drukt debug info af wat microcontroller terugstuurt
def printserialout():
    out = ser.read_until()
    out.decode('ascii')
    print(bytes(out))
    out = ser.read_until()
    out.decode('ascii')
    print(bytes(out))
    out = ser.read_until()
    out.decode('ascii')
    print(bytes(out))
    out = ser.read_until()
    out.decode('ascii')
    print(bytes(out))
    return;


#send functie
def sendLed (rood, groen, blauw):

    ser.write(rood)
    #printserialout()
                
    ser.write(groen)
    #printserialout()
        
    ser.write(blauw)
    #printserialout()

    return;

#random color
def randomColor():
    C1 = 0
    C2 = 0
    C3 = 0
    C1 = random.randint(0,2)
    if C1 == 2:
        C2 = random.randint(0,5)
        if C2 == 5:
            C3 = random.randint(0,5)
        else:
            C3 = random.randint(0,9)
    else:
        C2 = random.randint(0,9)
        C3 = random.randint(0,9)
    C1 = str(C1)
    C2 = str(C2)
    C3 = str(C3)

    color = C1 + C2 + C3
    return color;
        
while 1 :
    
    rood = randomColor()
    groen = randomColor()
    blauw = randomColor()
    
    rood = rood.encode('ascii','replace')
    groen = groen.encode('ascii','replace')
    blauw = blauw.encode('ascii','replace')
    print(rood)
    print(groen)
    print(blauw)
    
    sendLed(rood,groen,blauw)
