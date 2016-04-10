import sys
import time
import serial
import asyncio
import random
import ledbol
import settings



R = '0'

while 1 :
    
    s = 1

    while s != 0:
        s = ledbol.USBinput()
    settings.rood = settings.R.encode('ascii','replace')
    print(R)
    print(rood)
