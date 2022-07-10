# Menu and Sub-menus in tkinter
# Message box in tkinter

from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("455x390")
root.title("Pycharm")

def myFunc():
    print("Details")
    
def help():
    tmsg.showinfo("Help", "This is GUI HelpBox and  I will help you!")
    
def rate():
    print("Rate Us")
    value = tmsg.askquestion("Rate", "You used this GUI.. Was your experieced Good?")
    if value == "yes":
        msg = "Great. Please rate us on app store"
    else:
        msg = "Tell us what went worng. We will call you soon for that"
    tmsg.showinfo("Experience", msg)
    
def divya():
    b = tmsg.askretrycancel("Divya se dhosti karle", "sorry divya nhi banegi apki dosth")
    if b:
        msg = "retry karne se b kuch nhi hoga"
    else:
        msg = "accha huva cancel kardiya varna peththi"
    tmsg.showinfo("karma", msg)
    
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

m3 = Menu(mainmenu, tearoff=0)
m3.add_command(label="Help", command=help)
m3.add_command(label="Rate Us", command=rate)



root.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)
mainmenu.add_cascade(label="Edit", menu=m2)
mainmenu.add_cascade(label="Selection")
mainmenu.add_cascade(label="Help", menu=m3)
mainmenu.add_cascade(label="BeFriend Divya", command=divya)
mainmenu.add_cascade(label="Exit", command=quit)




root.mainloop() 