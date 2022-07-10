from tkinter import *
root = Tk()
root.geometry("455x300")
root.title("Listbox Tutorial")


def addmore():
    items = ["pavbaji", "uttappa", "daal", "panipuri"]
    lbx.insert(ACTIVE, items[0])
    lbx.insert(ACTIVE, items[1])
    lbx.insert(ACTIVE, items[2])
    lbx.insert(ACTIVE, items[3])

lbx = Listbox(root)
lbx.pack()
lbx.insert(END, "Add more items!")

Button(root, text="Add more", command=addmore).pack()

root.mainloop()