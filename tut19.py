from tkinter import *
root = Tk()
root.geometry("800x600")
root.wm_iconbitmap("notepad.ico")
root.title('Notepad++')
root.configure(bg="grey")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
print(f"{width}x{height}")

Button(text="click", command=root.destroy).pack()



root.mainloop()