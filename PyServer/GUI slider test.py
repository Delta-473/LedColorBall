from tkinter import *

import serial

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


####################
# Functies Declaraties #
####################

def printrood(roods):
    global rood
    rood = roods
    print("rood: ", rood)
    printkleur()
    send()
    return


def printgroen(groens):
    global groen
    groen = groens
    print("groen: ", groen)
    printkleur()
    send()
    return


def printblauw(blauws):
    global blauw
    blauw = blauws
    print("blauw: ", blauw)
    printkleur()
    return


def printkleur():
    global rood
    global groen
    global blauw

    print("rood: ", rood, "groen: ", groen, "blauw: ", blauw)
    return


# send functie
def send_led():
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

    stop = 'E'
    ser.write(stop)

    return


def convert(color):
    c1 = 0
    c2 = 0
    c3 = 0

    if color < 100:
        c1 = str(color)
        c2 = str(0)
        color = c2 + c1
        return color

    elif color == 0:
        c1 = str(c1)
        c2 = str(c2)
        c3 = str(c3)
        color = c1 + c2 + c3
        return color

    else:
        color = str(color)
        return color



def send():
    global rood
    global groen
    global blauw

    printkleur()

    rood = convert(rood)
    groen = convert(groen)
    blauw = convert(blauw)

    send_led()

    return


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
