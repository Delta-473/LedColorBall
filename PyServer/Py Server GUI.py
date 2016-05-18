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
    return


def set_time(itijd):
    global tijd
    tijd = itijd


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
    w = Scale(master, from_=0, to=2, resolution=0.1, orient=HORIZONTAL, command=set_time)
    w.pack()
    fred = Button(master, fg="black", bg="green", text="random kleur", command=core.en_random_color)
    fred.pack()
    master.mainloop()
    return


rand = PyServerCore.RandomColor()
GUI_thread = Thread(target=main_gui)
ServerCore_thread = Thread(target=PyServerCore.ServerCore)
RandomNumber_thread = Thread(target=rand.random_color)
GUI_thread.start()
ServerCore_thread.start()
RandomNumber_thread.start()
