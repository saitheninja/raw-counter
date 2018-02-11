from tkinter import *


rootWindow = Tk()

filetypeFrame = Frame(rootWindow)
filetypeFrame.pack(side=TOP)

raf = IntVar()
check1 = Checkbutton(filetypeFrame, text="RAF", variable=raf).grid(row=0)
nef = IntVar()
check2 = Checkbutton(filetypeFrame, text="NEF", variable=nef).grid(row=1)
cr2 = IntVar()
check3 = Checkbutton(filetypeFrame, text="CR2", variable=cr2).grid(row=2)


rafTotal = 0
nefTotal = 0
cr2Total = 0


if raf == 1:
    for dirpath, dirnames, filenames in os.walk("D:\!!!! Potatoes"):
        for file in filenames:
            if file.endswith(".NEF"):
                rafTotal += 1
else:
    print("no")

if nef == 1:
    for dirpath, dirnames, filenames in os.walk("D:\!!!! Potatoes"):
        for file in filenames:
            if file.endswith(".NEF"):
                nefTotal += 1

if cr2 == 1:
    for dirpath, dirnames, filenames in os.walk("D:\!!!! Potatoes"):
        for file in filenames:
            if file.endswith(".NEF"):
                cr2Total += 1


rootWindow.mainloop()