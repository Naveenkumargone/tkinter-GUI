# Menu and Sub-menus in tkinter
from tkinter import *
root = Tk()
root.geometry("455x390")

def myFunc():
    print("Details")

# #use these to create  a non dropdown menu
# myMenu = Menu(root)
# myMenu.add_command(label="File", command=myFunc)
# myMenu.add_command(label="Exit", command=quit)
# root.config(menu=myMenu)


mainmenu = Menu(root)
m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="New Project", command=myFunc)
m1.add_command(label="Save", command=myFunc)
m1.add_command(label="Save As", command=myFunc)
m1.add_separator()
m1.add_command(label="Open", command=myFunc)    
m1.add_command(label="Print", command=myFunc)

m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut", command=myFunc)
m2.add_command(label="Copy", command=myFunc)
m2.add_command(label="Paste", command=myFunc)
m2.add_separator()
m2.add_command(label="Undo", command=myFunc)    
m2.add_command(label="Redo", command=myFunc)

root.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)
mainmenu.add_cascade(label="Edit", menu=m2)
mainmenu.add_cascade(label="Selection")
mainmenu.add_cascade(label="Exit", command=quit)



root.mainloop() 