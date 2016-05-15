import serial


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

    #################
    # Globale Variable #
    #################
    global rood
    global groen
    global blauw

    rood = '000'
    groen = '000'
    blauw = '000'

    # send functie
    def sendLed(self):
        global rood
        global groen
        global blauw

        version = 'S'
        ServerCore.ser.write(version)
        rood = rood.encode('ascii', 'replace')
        ServerCore.ser.write(rood)
        # ServerCore.printserialout()

        groen = groen.encode('ascii', 'replace')
        ServerCore.ser.write(groen)
        # ServerCore.printserialout()

        blauw = blauw.encode('ascii', 'replace')
        ServerCore.ser.write(blauw)
        # ServerCore.printserialout()

        stop = 'E'
        ServerCore.ser.write(stop)

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

        ServerCore.sendLed(self)

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
