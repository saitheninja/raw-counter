# import folder commands
import os
# import gui stuff
from tkinter import *


# counter
class CounterClass:
    # setup variables
    Total = 0
    display = "1"

    def __init__(self, filetype):
        self.filetype = filetype
        self.folderFrame = FolderFrame()

    # count
    def filetypecounter(self):
        for dirpath, dirnames, filenames in os.walk("D:\!!!! Potatoes"):     #D:\!!!! Potatoes
            for file in filenames:
                if file.endswith("." + self.filetype):
                    self.Total += 1
        self.updatetotals()

    # update totals
    def updatetotals(self):
        print("%d %ss" % (self.Total, self.filetype))
        self.display = (str(self.Total) + " " + self.filetype + "s")


# folder input
class FolderFrame:
    def __init__(self):
        # draw location input frame
        self.locationFrame = Frame(rootWindow)
        self.locationFrame.pack(side=BOTTOM)

        # location input text and textbox
        self.folderLocation = Label(self.locationFrame, text="Folder:")
        self.folderLocation.pack()
        self.locationEntry = Entry(self.locationFrame)
        self.locationEntry.pack()

    # def for locationstr
    def return_entry(self):
        location = locationEntry.get()
        print(location)


# checkboxes, because I guess why not
class CheckBoxes:
    self.onoff = IntVar()

    def __init__(self):
        #might need to change rootWindow to something more general
        self.checkboxFrame = Frame(rootWindow)
        self.checkboxFrame.pack()

        self.filetype = filetype
        Checkbutton(checkboxFrame, text="RAF", variable=raf, onvalue="1", offvalue="0", command=rafcount).grid(
            row=0)



# draw root window
rootWindow = Tk()


# draw filetype frame





# create create new class instance for each filetype checked
rafcounter = CounterClass("RAF")
nefcounter = CounterClass("NEF")


# function to check checkboxes
def rafcount():
    if raf.get() == 1:
        return_entry()
        rafcounter.Total = 0
        rafcounter.filetypecounter()
    else:
        pass

def nefcount():
    if nef.get() == 1:
        return_entry()
        nefcounter.Total = 0
        nefcounter.filetypecounter()
    else:
        pass


# draw checkboxes, give them variables
#raf = IntVar()
#check1 = Checkbutton(filetypeFrame, text="RAF", variable=raf, onvalue="1", offvalue="0", command=rafcount).grid(row=0)
#nef = IntVar()
#check2 = Checkbutton(filetypeFrame, text="NEF", variable=nef, onvalue="1", offvalue="0", command=nefcount).grid(row=1)
#cr2 = IntVar()
#check3 = Checkbutton(filetypeFrame, text="CR2", variable=cr2, onvalue="1", offvalue="0").grid(row=2)


# draw counter labels, create variables
raflabel = Label(filetypeFrame, textvariable=rafcounter.display).grid(row=0, column=1)
neflabel = Label(filetypeFrame, textvariable=nefcounter.display).grid(row=1, column=1)


rootWindow.mainloop()
