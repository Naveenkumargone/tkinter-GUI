# classess and objects in tkinter

from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("755x650")
        
    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.st = Label(self, textvariable=self.var)
        self.st.pack(side=BOTTOM, fill=X)
    
    def click(self):
        print("Button clicked")
        
    
    def createbutton(self, inptext):
        Button(text=inptext, command=self.click).pack()
    
    
if __name__ == '__main__':
    window = GUI()
    window.status()
    window.click()
    window.createbutton("clickme")
    window.mainloop()    ## window is root now