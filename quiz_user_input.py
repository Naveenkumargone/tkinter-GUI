#Create a GUI window that takes the input of width and height
# Create a Button "Apply" and after clicking on this button it will 
# change the size of the GUI window accordingly
# Code as described/written in the video

from tkinter import *

def getvals():
    root.geometry(f"{width.get()}x{height.get()}")

root = Tk()
root.geometry("400x455")


label = Label(text="😎 Do you want to change the Width and Height of this window size,", font="lucida 10 bold")
label2 = Label(text=" Then Please enter input of the Width and Height of your choice", font="Calibri 10 bold")
label.pack()
label2.pack()

width = StringVar()
height = StringVar()

widthentry = Entry(root, textvariable=width).pack()
heightentry = Entry(root, textvariable=height).pack()

Button(root, text="Submit", command=getvals).pack()


root.mainloop()
