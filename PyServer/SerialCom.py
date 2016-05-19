import sys
import time
import serial
import asyncio
#import ledbol

print ("Python Serial Ledbol Server Terminal V0.1\n")

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
global R
global G
global B
R = 0
G = 0
B = 0

null = 0
byte = 0
global rood
global groen
global blauw

#count amount of characters in a string
def countinput(str):
    counter = len(str)
    return counter;

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

#input
def USBinput():
    #global voor de variable zetten zorgt ervoor dat de waarde van
    #variable globaal wordt aangepast
    global R
    global G
    global B
    #get keyboard input
    R = input("Enter Red >> ")
    S = checkinput(R)           #S is status
    if S == 1:
        return S;
    
    counter = countinput(R)
    if counter != 3:
        S = 1;
        print("ERROR: Invalid value\n")
        return S
    
    G = input("Enter Green >> ")
    S = checkinput(G)
    if S == 1:
        return S;
    
    counter = countinput(G)
    if counter != 3:
        S = 1;
        print("ERROR: Invalid value\n")
        return S
    
    B = input("Enter Blue >> ")
    S = checkinput(B)
    if S == 1:
        return S;
    
    counter = countinput(B)
    if counter != 3:
        S = 1;
        print("ERROR: Invalid value\n")
        return S
    
    return S;

#check input
def checkinput(str):

    if R == 'exit':
        ser.close()
        exit()
    elif G == 'exit':
        ser.close()
        exit()
    elif B == 'exit':
        ser.close()
        exit()
    elif R == 'reset':
        return 1;
    elif G == 'reset':
        return 1;
    elif B == 'reset':
        return 1; 
    else:
        return 0;

#send functie
def sendLed (rood, groen, blauw):


    version = 'S'
    version = version.encode('ascii','replace')
    ser.write(version)
    ser.write(rood)
    #printserialout()
                
    ser.write(groen)
    #printserialout()
        
    ser.write(blauw)
    #printserialout()

    Stop = 'E'
    Stop = Stop.encode('ascii','replace')
    ser.write(Stop)

    return;
 
while 1 :
    s = 1
    #get keyboard input
    while s != 0:
        s = USBinput()
    r = int (R)
    g = int (G)
    b = int (B)
    rood = R.encode('ascii','replace')
    groen = G.encode('ascii','replace')
    blauw = B.encode('ascii','replace')
    print(R)
    print(rood)
    print(G)
    print(groen)
    print(B)
    print(blauw)
        
    sendLed(rood, groen, blauw)
