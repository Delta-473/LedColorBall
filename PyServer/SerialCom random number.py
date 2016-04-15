import sys
import time
import serial
import asyncio
import random
import ledbol

print ("Python Serial Ledbol Random Number Server Terminal V0.1\n")

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
