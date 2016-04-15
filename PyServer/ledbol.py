import sys
import random
import serial

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

global R
R = 0
global G
G = 0
global B
B = 0
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


#send functie
def sendLed (rood, groen, blauw):

    version = '001'
    version = version.encode('ascii','replace')
    ser.write(version)
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
