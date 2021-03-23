#!/usr/bin/python3
#HelloTk
from tkinter import *

class Application(Frame):
    def nameit(self):
        print("hi there, everyone!")

    def sayit(self):
        print("I push my fingers into my eyes")

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Now this is just a bigbutton"
        self.hi_there["fg"] = "green"
        self.hi_there["command"] = self.nameit

        self.hi_there.pack({"side": "left"})

        #muh ha ha ha ha
        #me learny program
        self.tog = Button(self)
        self.tog["text"] = "I will say what I need to say"
        self.tog["fg"] = "blue"
        self.tog["command"] = self.sayit

        self.tog.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
