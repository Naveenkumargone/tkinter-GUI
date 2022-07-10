# Creating RadioButtons in tkinter

from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("500x490")
root.title("RadioButton Tutorial")

def order():    
    tmsg.showinfo("Order Received!", f"We have received your order {var.get()}. Thanks for ordering")

var = StringVar()
var.set("Radio")
Label(root, text="What would you like to have sir?", font="Lucida 18 bold").pack()
for i in range(4):
    list = ["Dosa", "Uttappa", "Idli", "VadaPav"]
    value = ["Dosa", "Uttappa", "Idli", "VadaPav"]
    radio = Radiobutton(root, text=list[i], padx=30, pady=10, variable=var, value=value[i]).pack(anchor='w')

Button(text="Order Now", command=order).pack()

root.mainloop()