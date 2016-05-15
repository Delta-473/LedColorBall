from threading import Thread
from tkinter import *

import PyServerCore


def printrood(irood):
    global rood
    rood = PyServerCore.ServerCore.convert(int(irood))
    rood = rood.encode('ascii', 'replace')
    print("rood: ", rood)

    printkleur()
    return


def printgroen(igroen):
    global groen
    groen = PyServerCore.ServerCore.convert(int(igroen))
    groen = groen.encode('ascii', 'replace')
    print("groen: ", groen)
    printkleur()
    return


def printblauw(iblauw):
    global blauw
    blauw = PyServerCore.ServerCore.convert(int(iblauw))
    blauw = blauw.encode('ascii', 'replace')
    print("blauw: ", blauw)
    printkleur()
    return


def printkleur():
    global rood
    global groen
    global blauw

    core = PyServerCore.ServerCore()

    print("rood: ", rood, "groen: ", groen, "blauw: ", blauw)
    core.send_led(rood, groen, blauw)
    #send_led()
    return


def send_led():
    global rood
    global groen
    global blauw

    version = 'S'
    version = version.encode('ascii', 'replace')
    PyServerCore.ServerCore.ser.write(version)
    # printserialout2()

    PyServerCore.ServerCore.ser.write(rood)
    # printserialout()

    PyServerCore.ServerCore.ser.write(groen)
    # printserialout()

    PyServerCore.ServerCore.ser.write(blauw)
    # printserialout()

    stop = 'E'
    stop = stop.encode('ascii', 'replace')
    PyServerCore.ServerCore.ser.write(stop)
    # printserialout2()

    return


#################
# Main Programma #
#################
def main_gui():
    master = Tk()
    master.title("Python GUI Server")
    master.geometry("350x200")

    core = PyServerCore.ServerCore()

    roodslider = Scale(master, from_=255, to=0, command=printrood)
    roodslider.pack(side="left")  # geldige opties zijn left, right, top, bottom
    groenslider = Scale(master, from_=255, to=0, command=printgroen)
    groenslider.pack(side="left")
    blauwslider = Scale(master, from_=255, to=0, command=printblauw)
    blauwslider.pack(side="left")
    w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
    w.pack()
    fred = Button(master, fg="black", bg="green", text="random kleur", command=core.random_color)
    fred.pack()
    master.mainloop()
    return


GUI_thread = Thread(target=main_gui)
ServerCore_thread = Thread(target=PyServerCore.ServerCore)
GUI_thread.start()
ServerCore_thread.start()
