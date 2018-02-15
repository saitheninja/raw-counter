# import folder commands
import os
# import gui stuff
from tkinter import *


# counter
class CounterClass:
    def __init__(self, filetype):
        # setup variables
        self.filetype = filetype
        self.Total = 0
        self.display = "1"

    # count
    def filetypecounter(self):
        for dirpath, dirnames, filenames in os.walk(folderClass.location):     # D:\!!!! Potatoes
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
    # change to grab current folder location
    location = "D:\!!!! Potatoes"

    def __init__(self):
        # draw location input frame
        self.locationFrame = Frame(rootWindow)
        self.locationFrame.pack(side=TOP)

        # location input text and textbox
        self.folderLocation = Label(self.locationFrame, text="Folder:")
        self.folderLocation.pack()
        self.locationEntry = Entry(self.locationFrame, textvariable=self.location)
        self.locationEntry.pack()


# checkboxes, because I guess why not
class CheckBoxes:
    def __init__(self):
        self.onOff = IntVar()
        for i in range(l):
            self.cBox = Checkbutton(checkboxFrame, text=allRaws[i], variable=self.onOff, onvalue=1, offvalue=0,
                               command=self.countstuff(i))
            self.cBox.grid(row=i)

    def countstuff(self, i):
        self.counter = CounterClass(allRaws[i])
        self.labelTotal = CounterLabel
        total[i] = self.counter.Total



class CounterLabel:
    # draw counter labels, create variables
    def __init__(self):
        self.label = Label(checkboxFrame, text=(total[i] + " " + allRaws[i]))
        self.label.grid(row=i, column=1)


# draw root window
rootWindow = Tk()
# draw folder entry frame
folderClass = FolderFrame()
# draw checkbox frame
checkboxFrame = Frame(rootWindow)
checkboxFrame.pack()


# all raw filetypes, from Wikipedia
allRaws = [".3fr",
".ari", ".arw",
".bay",
".crw", ".cr2",
".cap",
".data", ".dcs", ".dcr", ".dng",
".drf",
".eip", ".erf",
".fff",
".gpr",
".iiq",
".k25", ".kdc",
".mdc", ".mef", ".mos", ".mrw",
".nef", ".nrw",
".obm", ".orf",
".pef", ".ptx", ".pxn",
".r3d", ".raf", ".raw", ".rwl", ".rw2", ".rwz",
".sr2", ".srf", ".srw",
".tif",
".x3f"]
# find length of list
l = len(allRaws)
# make list of zeroes, length l
total = [0] * l

i = 0
cb = CheckBoxes()

"""# create a checkbox for each entry in the list
i = 0
onOff = Variable()
rangeList = [range(l)]
for i in range(l):
    cBox = Checkbutton(checkboxFrame, text=allRaws[i], variable=onOff, command=countStuff(i))
    cBox.grid(row=i)
"""

rootWindow.mainloop()
