import sys
import time
import serial
from tkinter import *

#####################
# Seriële communicatie #
#####################

# open config file
# TODO: Add exception when config is missing cannot be opend.
config = open("config.txt", "r")

COM = config.readline()
COM = COM.replace("SERIALPORT: ", "", 1)
COM = COM.rstrip('\n')  # stripping newline charachter

BAUD = config.readline()
BAUD = BAUD.replace("BAUDRATE: ", "", 1)
BAUD = BAUD.rstrip('\n')

print("DEBUG: opening config file succesfull\n")

# configure the serial connection
ser = serial.Serial(
    port=COM,
    baudrate=BAUD,
    parity=serial.PARITY_NONE,  # uitlezen vanuit configbestand werkt nog niet
    stopbits=serial.STOPBITS_ONE,  # geeft error vb: serial.PARITY module serial
    bytesize=serial.EIGHTBITS  # has no attribute 'PARITY'
)

ser.isOpen()

#################
# Globale Variable #
#################
global rood
global groen
global blauw

rood = 0
groen = 0
blauw = 0


####################
# Functies Declaraties #
####################

def printrood(roods):
    global rood
    rood = roods
    print("rood: ", rood)
    printkleur()
    Send()
    return;


def printgroen(groens):
    global groen
    groen = groens
    print("groen: ", groen)
    printkleur()
    Send()
    return;


def printblauw(blauws):
    global blauw
    blauw = blauws
    print("blauw: ", blauw)
    printkleur()
    return;


def printkleur():
    global rood
    global groen
    global blauw

    print("rood: ", rood, "groen: ", groen, "blauw: ", blauw)
    return;


# send functie
def sendLed():
    global rood
    global groen
    global blauw

    version = 'S'
    # version = version.encode('ascii','replace')
    ser.write(version)
    rood = rood.encode('ascii', 'replace')
    ser.write(rood)
    # printserialout()

    groen = groen.encode('ascii', 'replace')
    ser.write(groen)
    # printserialout()

    blauw = blauw.encode('ascii', 'replace')
    ser.write(blauw)
    # printserialout()

    Stop = 'E'
    ser.write(Stop)

    return;


def Convert(Color):
    C1 = 0
    C2 = 0
    C3 = 0

    if Color < 100:
        C1 = str(Color)
        C2 = str(0)
        Color = C2 + C1
        return Color;

    elif Color == 0:
        C1 = str(C1)
        C2 = str(C2)
        C3 = str(C3)
        Color = C1 + C2 + C3
        return Color;

    else:
        Color = str(Color)
        return Color;

    return;


def Send():
    global rood
    global groen
    global blauw

    printkleur()

    rood = Convert(rood)
    groen = Convert(groen)
    blauw = Convert(blauw)

    sendLed()

    return;


#################
# Main Programma #
#################

master = Tk()
master.title("Python GUI Server")
master.geometry("350x200")

roodslider = Scale(master, from_=255, to=0, command=printrood)
roodslider.pack(side="left")  # geldige opties zijn left, right, top, bottom
groenslider = Scale(master, from_=255, to=0, command=printgroen)
groenslider.pack(side="left")
blauwslider = Scale(master, from_=255, to=0, command=printblauw)
blauwslider.pack(side="left")
w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
w.pack()
fred = Button(master, fg="red", bg="green")
fred.pack()
master.mainloop()
