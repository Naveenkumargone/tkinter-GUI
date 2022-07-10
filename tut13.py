# Sliders in tkinter using Scale()

from tkinter import * 
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("500x490")
root.title("Slider Tutorial")

def getdollars():
    print(f"We have credited {slider2.get()} to your bank account")
    tmsg.showinfo("Amount Credited", f"We have credited {slider2.get()} to your bank account")

# slider1 = Scale(root, from_=0, to=100)
# slider1.pack()
Label(root, text='How many dollars you want?').pack()
slider2 = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=50)
slider2.set(34)
slider2.pack()

Button(root, text='Get Dollars $', command=getdollars).pack()



root.mainloop()