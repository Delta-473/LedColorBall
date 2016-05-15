from threading import Thread
from tkinter import *
import PyServerCore


def printrood(irood):
    global rood
    rood = PyServerCore.ServerCore.Convert(int(irood))
    rood = rood.encode('ascii', 'replace')
    print("rood: ", rood)

    printkleur()
    return


def printgroen(igroen):
    global groen
    groen = PyServerCore.ServerCore.Convert(int(igroen))
    groen = groen.encode('ascii', 'replace')
    print("groen: ", groen)
    printkleur()
    return


def printblauw(iblauw):
    global blauw
    blauw = PyServerCore.ServerCore.Convert(int(iblauw))
    blauw = blauw.encode('ascii', 'replace')
    print("blauw: ", blauw)
    printkleur()
    return


def printkleur():
    global rood
    global groen
    global blauw

    #PyServerCore.Convert()

    print("rood: ", rood, "groen: ", groen, "blauw: ", blauw)
    #PyServerCore.ServerCore.Send()
    sendLed()
    return

def sendLed():
    global rood
    global groen
    global blauw

    version = 'S'
    version = version.encode('ascii', 'replace')
    PyServerCore.ServerCore.ser.write(version)
    #printserialout2()

    PyServerCore.ServerCore.ser.write(rood)
    #printserialout()


    PyServerCore.ServerCore.ser.write(groen)
    #printserialout()


    PyServerCore.ServerCore.ser.write(blauw)
    #printserialout()

    Stop = 'E'
    Stop = Stop.encode('ascii', 'replace')
    PyServerCore.ServerCore.ser.write(Stop)
    #printserialout2()

    return

def printserialout():
    out = PyServerCore.ServerCore.ser.read_until()
    out.decode('ascii')
    print(bytes(out))
    out = PyServerCore.ServerCore.ser.read_until()
    out.decode('ascii')
    print(bytes(out))
    out = PyServerCore.ServerCore.ser.read_until()
    out.decode('ascii')
    print(bytes(out))
    out = PyServerCore.ServerCore.ser.read_until()
    out.decode('ascii')
    print(bytes(out))
    return
def printserialout2():
    out = PyServerCore.ServerCore.ser.read_until()
    out.decode('ascii')
    print(bytes(out))

    return
#################
# Main Programma #
#################
def main_gui():
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
    return


GUI_thread = Thread(target=main_gui)
ServerCore_thread = Thread(target=PyServerCore.ServerCore)
GUI_thread.start()
ServerCore_thread.start()
