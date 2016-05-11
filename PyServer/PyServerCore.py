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

    rood = 0
    groen = 0
    blauw = 0

    # send functie
    def sendLed(self):
        global rood
        global groen
        global blauw

        version = 'S'
        # version = version.encode('ascii','replace')
        ServerCore.ser.write(version)
        rood = rood.encode('ascii', 'replace')
        ServerCore.ser.write(rood)
        # printserialout()

        groen = groen.encode('ascii', 'replace')
        ServerCore.ser.write(groen)
        # printserialout()

        blauw = blauw.encode('ascii', 'replace')
        ServerCore.ser.write(blauw)
        # printserialout()

        Stop = 'E'
        ServerCore.ser.write(Stop)

        return

    def Convert(Color):
        c1 = 0
        c2 = 0
        C3 = 0

        if Color < 100:
            c1 = str(Color)
            c2 = str(0)
            Color = c2 + c1
            return Color

        elif Color == 0:
            c1 = str(c1)
            c2 = str(c2)
            C3 = str(C3)
            Color = c1 + c2 + C3
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
