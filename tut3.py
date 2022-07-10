# Attributes of Label and Pack

from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.geometry("744x133")
root.title("Swamy Vivekananda")

''' Important Label Options
text - adds the text
bg - background
fg - foreground
font - sets the font
1. font=("comicsansms", 19, "bold")
2. font="comicsansms 19 bold"
padx - x padding
pady - y padding
relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE ''' #relief means border kaise dikhna chayiye 

image = Image.open("sv.jpg")
photo = ImageTk.PhotoImage(image)   

Naveen_label = Label(image=photo, padx=10, pady=10, borderwidth=15, relief=SUNKEN)
Naveen_label.pack(side=LEFT, fill=Y, padx=34, pady=34)

text2=Label(text="About Swamy Vivekananda", padx=2, pady=50, font="Calibri 20 bold", borderwidth=3)
text2.pack()

title_label = Label(text ='''
Swami Vivekananda (/ˈSwɑːmi ˌVɪveɪˈkɑːnəndə/; Bengali: [ʃami bibekanɔndo] (audio speaker iconlisten); 
12 January 1863 – 4 July 1902), born Narendranath Datta (Bengali: [nɔrendronatʰ dɔto]),
was an Indian Hindu monk and philosopher.
He was a chief disciple of the 19th-century Indian mystic Ramakrishna.
[12] He was a major force in the contemporary Hindu reform movements in India, 
and contributed to the concept of nationalism in colonial India.
[13] Vivekananda founded the Ramakrishna Math and the Ramakrishna Mission.
[10] He is perhaps best known for his speech which began with the words "Sisters and brothers of America ...,
"[14] in which he introduced Hinduism at the Parliament of the World's Religions in Chicago in 1893.''',
bg ="Blue", fg="white", padx=13, pady=50, font="Calibri 12 bold", borderwidth=3, relief=SUNKEN)

# Important Pack options
# anchor = nw
# side = top, bottom, left, right
# fill
# padx
# pady

# title_label.pack(side=BOTTOM, anchor ="sw", fill=X)
title_label.pack(side=LEFT, fill=Y, padx=34, pady=34)


root.mainloop()


