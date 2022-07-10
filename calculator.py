from tkinter import *

# event.widget gets the value of that number,and cget function gets text of that widget
def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())  #eval func returns str(num) into int(num)

            except Exception as e:
                print(e)
                value = "Error" 
            
        scvalue.set(value)
        screen.update()
        
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
        

root = Tk()
root.geometry("550x650")
root.title("This Calculator is Developed by NG😎")
root.wm_iconbitmap("calculator.ico")

        
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvariable=scvalue, font="lucida 30 bold")
screen.pack(fill=X, ipadx=12, padx=10, pady=10)


f = Frame(root, bg="grey")
b = Button(f, text="C", padx=28, pady=22, bg="orange", fg="red",font="lucida 18 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=8, pady=8)
f.pack()

b = Button(f, text=".", padx=28, pady=22, font="lucida 18 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=8, pady=8)
f.pack()

b = Button(f, text="0", padx=28, pady=22, font="lucida 18 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=8, pady=8)
f.pack()

b = Button(f, text="=", padx=28, pady=22, fg="red", font="lucida 18 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=8, pady=8)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="7", padx=28, pady=22, font="lucida 18 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=8, pady=8)
f.pack()

b = Button(f, text="8", padx=28, pady=22, font="lucida 18 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=8, pady=8)
f.pack()

b = Button(f, text="9", padx=28, pady=22, font="lucida 18 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=8, pady=8)
f.pack()


b = Button(f, text="+", padx=3, pady=20, fg="red", font="lucida 18 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=1, pady=10)
f.pack()

b = Button(f, text="/", padx=7, pady=20, fg="red", font="lucida 18 bold")
b.bind("<Button-1>", click)
b.pack(side=LEFT, padx=10, pady=10)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="4", padx=28, pady=22, font="lucida 18 bold")
b.pack(side=LEFT, padx=8, pady=8)
b.bind("<Button-1>", click)
f.pack()



b = Button(f, text="5", padx=28, pady=22, font="lucida 18 bold")
b.pack(side=LEFT, padx=8, pady=8)
b.bind("<Button-1>", click)
f.pack()


b = Button(f, text="6", padx=28, pady=22, font="lucida 18 bold")
b.pack(side=LEFT, padx=8, pady=8)
b.bind("<Button-1>", click)
f.pack()

b = Button(f, text="-", padx=28, pady=22, fg="red",font="lucida 18 bold")
b.pack(side=LEFT, padx=10, pady=8)
b.bind("<Button-1>", click)
f.pack()


f = Frame(root, bg="grey")
b = Button(f, text="1", padx=28, pady=22, font="lucida 18 bold")
b.pack(side=LEFT, padx=8, pady=8)
b.bind("<Button-1>", click)
f.pack()


b = Button(f, text="2", padx=28, pady=22, font="lucida 18 bold")
b.pack(side=LEFT, padx=8, pady=8)
b.bind("<Button-1>", click)
f.pack()

b = Button(f, text="3", padx=28, pady=22, font="lucida 18 bold")
b.pack(side=LEFT, padx=8, pady=8)
b.bind("<Button-1>", click)
f.pack()

b = Button(f, text="*", padx=28, pady=22, fg="red", font="lucida 18 bold")
b.pack(side=LEFT, padx=9, pady=8)
b.bind("<Button-1>", click)
f.pack()






root.mainloop()