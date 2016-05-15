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
        ServerCore.printserialout()

        groen = groen.encode('ascii', 'replace')
        ServerCore.ser.write(groen)
        ServerCore.printserialout()

        blauw = blauw.encode('ascii', 'replace')
        ServerCore.ser.write(blauw)
        ServerCore.printserialout()

        Stop = 'E'
        ServerCore.ser.write(Stop)

        return

    def Convert(Color):
        c1 = '0'
        c2 = '0'
        c3 = '0'

        if Color < 100:
            c1 = str(Color)
            c2 = str(0)
            Color = c2 + c1
            if len(Color) == 2:
                Color = c2 + Color
            return Color

        elif Color == 0:

            Color = '000'
            return Color

        else:
            Color = str(Color)
            return Color

    def Send(self):
        global rood
        global groen
        global blauw

        rood = ServerCore.Convert(rood)
        groen = ServerCore.Convert(groen)
        blauw = ServerCore.Convert(blauw)

        ServerCore.sendLed()

        return

        #drukt debug info af wat microcontroller terugstuurt
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