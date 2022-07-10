# Status Bar Tutorial in tkinter

from tkinter import *

def upload():
    statusvar.set("Progress... Please wait")
    st.update()
    import time
    time.sleep(3)
    statusvar.set("Upload Complete")

root = Tk()
root.geometry("455x233")
root.title("Statusbar tutorial")



statusvar = StringVar()
statusvar.set("Ready")
st = Label(root, textvariable=statusvar)
st.pack(side=BOTTOM, anchor="w")

Button(root, text="Upload", command=upload).pack()



root.mainloop()