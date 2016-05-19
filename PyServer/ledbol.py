import random

import serial

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


# count amount of characters in a string
def count_input(str):
    counter = len(str)
    return counter


# drukt debug info af wat microcontroller terugstuurt
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
    return


def printserialout2():
    out = ser.read_until()
    out.decode('ascii')
    return


# send functie
def send_led(rood, groen, blauw):
    version = 'S'
    version = version.encode('ascii', 'replace')
    # printserialout2()
    ser.write(version)
    ser.write(rood)
    # printserialout()

    ser.write(groen)
    # printserialout()

    ser.write(blauw)
    # printserialout()

    stop = 'E'
    stop = stop.encode('ascii', 'replace')
    ser.write(stop)
    # printserialout2()

    return


# random color
def random_color():
    c1 = random.randint(0, 2)
    if c1 == 2:
        c2 = random.randint(0, 5)
        if c2 == 5:
            c3 = random.randint(0, 5)
        else:
            c3 = random.randint(0, 9)
    else:
        c2 = random.randint(0, 9)
        c3 = random.randint(0, 9)
    c1 = str(c1)
    c2 = str(c2)
    c3 = str(c3)

    color = c1 + c2 + c3
    return color


# input
def usb_input():
    # global voor de variable zetten zorgt ervoor dat de waarde van
    # variable globaal wordt aangepast
    global r
    global g
    global b
    # get keyboard input
    r = input("Enter Red >> ")
    s = check_input()  # s is status
    if s == 1:
        return s

    counter = count_input(r)
    if counter != 3:
        s = 1
        print("ERROR: Invalid value\n")
        return s

    g = input("Enter Green >> ")
    s = check_input()
    if s == 1:
        return s

    counter = count_input(g)
    if counter != 3:
        s = 1
        print("ERROR: Invalid value\n")
        return s

    b = input("Enter Blue >> ")
    s = check_input()
    if s == 1:
        return s

    counter = count_input(b)
    if counter != 3:
        s = 1
        print("ERROR: Invalid value\n")
        return s

    return s


# check input
def check_input():
    if r == 'exit':
        ser.close()
        exit()
    elif g == 'exit':
        ser.close()
        exit()
    elif b == 'exit':
        ser.close()
        exit()
    elif r == 'reset':
        return 1
    elif g == 'reset':
        return 1
    elif b == 'reset':
        return 1
    else:
        return 0
