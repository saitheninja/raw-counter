# Counts total number of Nikon and Fuji raws in photo folder
# https://stackoverflow.com/questions/1320731/count-number-of-files-with-certain-extension-in-python

import os
from tkinter import *
import tkinter.messagebox

total = 0



class FileTypes:
    def __init__(self, rootWindow):
        rootWindow = rootWindow
        filetypeFrame = Frame(rootWindow)
        filetypeFrame.pack(side=TOP)

        self.raf = IntVar()
        check1 = Checkbutton(filetypeFrame, text="RAF", variable=raf).grid(row=0)
        self.nef = IntVar()
        check2 = Checkbutton(filetypeFrame, text="NEF", variable=nef).grid(row=1)
        self.cr2 = IntVar()
        check3 = Checkbutton(filetypeFrame, text="CR2", variable=cr2).grid(row=2)

    def checkFileTypes(self):
        print("later.")





















for dirpath, dirnames, filenames in os.walk("D:\!!!! Potatoes"):
    for file in filenames:
        if file.endswith(".NEF"):
            total += 1
        elif file.endswith(".RAF"):
            total += 1


# popup with final total
#tkinter.messagebox.showinfo("window title", "You have made %d photographs." % total)




rootWindow = Tk()  # makes window

#locationFrame = Frame(rootWindow)
#locationFrame.pack(side=TOP)
#filetypeFrame = Frame(rootWindow)
#filetypeFrame.pack(side=TOP)
#buttonFrame = Frame(rootWindow)
#buttonFrame.pack(side=TOP)

#ob = FileTypes(filetypeFrame)

rootWindow.mainloop()  # keeps window open (i.e. doesn't just run and close