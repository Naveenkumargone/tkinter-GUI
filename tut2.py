from tkinter import *
from PIL import Image, ImageTk    #PIL means Python, library, Image helps to pack the jpg files in GUI

a_root = Tk()   # root is the instance of class Tk
                # basic gui create karti he 
                # basic gui components ready rakti he 

# width x height
a_root.geometry("1300x1200")

#width, height
a_root.minsize(200, 100)
a_root.maxsize(1400, 1400)

# a = Label(text="\nThis GUI is developed by NG😎\n")
# a.pack()
# photo = PhotoImage(file="Naveen.png")

#for JPG images
image = Image.open("Naveen.jpg")
photo = ImageTk.PhotoImage(image)   

Naveen_label = Label(image=photo)
Naveen_label.pack()

#gui logic here
a_root.mainloop()   #main loop is also called as event loop 
                    #gui window se interact karti he or gui ka logic ko yaad karvata he
# pack grid place 