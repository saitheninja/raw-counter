import os
from tkinter import *


# counter
class CounterClass:
    def counter(self):
        if raf.get() == 1:
            for dirpath, dirnames, filenames in os.walk("location"):
                for file in filenames:
                    if file.endswith(".RAF"):
                        rafTotal += 1
        print("%d RAFs" % rafTotal)

        if nef.get() == 1:
            for dirpath, dirnames, filenames in os.walk("location"):
                for file in filenames:
                    if file.endswith(".NEF"):
                        nefTotal += 1
        print("%d NEFs" % nefTotal)

        if cr2.get() == 1:
            for dirpath, dirnames, filenames in os.walk("location"):
                for file in filenames:
                    if file.endswith(".CR2"):
                        cr2Total += 1
        print("%d CR2s" % cr2Total)
        #D:\!!!! Potatoes


rootWindow = Tk()


# draw location input frame
locationFrame = Frame(rootWindow)
locationFrame.pack(side=TOP)


# def for locationstr
def return_entry():
    location = locationEntry.get()
    print(location)

# location input text and textbox
folderLocation = Label(locationFrame, text="Folder:")
folderLocation.pack()
locationEntry = Entry(locationFrame)
locationEntry.pack()





# draw filetype frame
filetypeFrame = Frame(rootWindow)
filetypeFrame.pack()


# draw checkboxes, give them variables
raf = IntVar()
check1 = Checkbutton(filetypeFrame, text="RAF", variable=raf).grid(row=0)
nef = IntVar()
check2 = Checkbutton(filetypeFrame, text="NEF", variable=nef).grid(row=1)
cr2 = IntVar()
check3 = Checkbutton(filetypeFrame, text="CR2", variable=cr2).grid(row=2)







# totals
rafTotal = 0
nefTotal = 0
cr2Total = 0

# draw status bar
finalText = "photographs made: %d RAFs, %d NEFs, %d CR2s." % (rafTotal, nefTotal, cr2Total)
status = Label(rootWindow, text=finalText, bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)






# count frame + button
countFrame = Frame(rootWindow)
countFrame.pack(side=BOTTOM)
callcounter = CounterClass
countButton = Button(countFrame, text="count", command=return_entry)
countButton.pack(pady=4)


rootWindow.mainloop()


# checkbox error checking
if raf.get() == 0 and nef.get() == 0 and cr2.get() == 0:
    finalText = "No file type chosen."


def counter(self):
    if raf.get() == 1:
        for dirpath, dirnames, filenames in os.walk("location"):
            for file in filenames:
                if file.endswith(".NEF"):
                    rafTotal += 1
    print("%d RAFs" % rafTotal)

    if nef.get() == 1:
        for dirpath, dirnames, filenames in os.walk("location"):
            for file in filenames:
                if file.endswith(".NEF"):
                    nefTotal += 1
    print("%d NEFs" % nefTotal)

    if cr2.get() == 1:
        for dirpath, dirnames, filenames in os.walk("location"):
            for file in filenames:
                if file.endswith(".NEF"):
                    cr2Total += 1
    print("%d CR2s" % cr2Total)
    # D:\!!!! Potatoes