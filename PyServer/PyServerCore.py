import serial
import random


#################
# Globale Variable #
#################
global rood
global groen
global blauw


class ServerCore():

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

    # send functie
    def send_led(self, rood, groen, blauw):

        version = 'S'
        version = version.encode('ascii', 'replace')
        ServerCore.ser.write(version)
        # printserialout2()

        ServerCore.ser.write(rood)
        # printserialout()

        ServerCore.ser.write(groen)
        # printserialout()

        ServerCore.ser.write(blauw)
        # printserialout()

        stop = 'E'
        stop = stop.encode('ascii', 'replace')
        ServerCore.ser.write(stop)
        # printserialout2()

        return

    def convert(color):

        if color < 100:
            c1 = str(color)
            c2 = str(0)
            color = c2 + c1
            if len(color) == 2:
                color = c2 + color
            return color

        elif color == 0:

            color = '000'
            return color

        else:
            color = str(color)
            return color

    def send(self):
        global rood
        global groen
        global blauw

        rood = ServerCore.convert(self, rood)
        groen = ServerCore.convert(self, groen)
        blauw = ServerCore.convert(self, blauw)

        ServerCore.send_led(self)

        return

        # drukt debug info af wat microcontroller terugstuurt

    def printserialout(self):
        out = ServerCore.ser.read_until()
        out.decode('ascii')
        print(bytes(out))
        out = ServerCore.ser.read_until()
        out.decode('ascii')
        print(bytes(out))
        out = ServerCore.ser.read_until()
        out.decode('ascii')
        print(bytes(out))
        out = ServerCore.ser.read_until()
        out.decode('ascii')
        print(bytes(out))
        return

    def printserialout2(self):
        out = ServerCore.ser.read_until()
        out.decode('ascii')
        print(bytes(out))

        return

    def random_color(self):
        global rood
        global groen
        global blauw

        rood = ServerCore.random_color_generator(self)
        groen = ServerCore.random_color_generator(self)
        blauw = ServerCore.random_color_generator(self)

        rood = rood.encode('ascii', 'replace')
        groen = groen.encode('ascii', 'replace')
        blauw = blauw.encode('ascii', 'replace')

        ServerCore.send_led(self, rood, groen, blauw)

        print(rood)
        print(groen)
        print(blauw)

        return

        # random color
    def random_color_generator(self):
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
