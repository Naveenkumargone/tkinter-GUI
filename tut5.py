from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("900x600")

def msg1():
    list = []
    for i in range(26):
        k = ord("A")+i
        print(chr(k), end=" ")
        list.append(chr(k))
    tmsg.showinfo("\n Alphabets are: ", f"The Alphabets are {list}")
        
def msg2():
    list = []
    i=1
    for i in range(21):
        list.append(i**2)
    tmsg.showinfo("\n\nsquares from 1-20", f"The Square Numbers are {list}")
        
def msg3():
    list = []
    i=1
    for i in range(21):
        list.append(i**3)
    tmsg.showinfo("\n\nCubes from 1-20", f"The Cube Numbers are {list}")

def msg4():
    list = []
    i=1
    for i in range(11):
        list.append(i*10)
    tmsg.showinfo("***** Table of 10 ***", f"Table of 10 is: {list}")
    
image = Image.open("sv.jpg")
photo = ImageTk.PhotoImage(image)   

Naveen_label = Label(image=photo, padx=10, pady=10, borderwidth=15, relief=SUNKEN)
Naveen_label.pack(side=LEFT, fill=Y, padx=34, pady=34)


  
text2=Label(text="This GUI developed by NG😎.", padx=10, pady=10, font="Calibri 20 bold", borderwidth=20)
text2.pack(anchor="n", side=TOP)

label = Label(text='''1. click on 1 to print the letters of alphabets,
2. click on 2 to print the square numbers,
3. click on 3 to print the cube numbers,
4. click on 4 to print the Table of 10''', font="calibri 16 bold", anchor="n",)
label.pack(side=TOP, fill=Y, anchor="n", padx=2, pady=2)

frame = Frame(root, borderwidth=1, )
frame.pack(side=TOP,anchor="s")

b1 = Button(frame, fg="red", text="1", command=msg1)
b1.pack(side=LEFT,anchor="n", padx=23)

b2 = Button(frame, fg="red", text="2", command=msg2)
b2.pack(side=LEFT,anchor="n", padx=23)

b3 = Button(frame, fg="red", text="3", command=msg3)
b3.pack(side=LEFT,anchor="n", padx=23)

b4 = Button(frame, fg="red", text="4", command=msg4)
b4.pack(side=LEFT,anchor="n", padx=23)

root.mainloop()

 