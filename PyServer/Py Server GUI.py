from threading import Thread
from tkinter import *
import PyServerCore


def printrood(roods):
    global rood
    rood = str(roods, 'ascii')
    print("rood: ", rood)
    rood = PyServerCore.ServerCore.Convert(rood)
    printkleur()
    return


def printgroen(groens):
    global groen
    groen = groens
    print("groen: ", groen)
    printkleur()
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

    PyServerCore.Convert()

    print("rood: ", rood, "groen: ", groen, "blauw: ", blauw)
    return


#################
# Main Programma #
#################
def main_gui():
    master = Tk()
    master.title("Python GUI Server")
    master.geometry("350x200")

    global rood
    global groen
    global blauw

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
