from tkinter import *
from tkinter import ttk
from tkinter import messagebox

win7 = Tk()
win7.title("GYM Management System")
win7.iconbitmap('icon.ico')
win7.maxsize(width= 1100,height = 760)
win7.minsize(width= 1100,height = 760)
# win.config(bg="yellow")

topheader = Frame(win7)
topheader.pack()
label = Label(topheader,text="GYM Management System").pack()

bg = PhotoImage(file = 'image_aboutus.png')
label = Label(win7,image=bg).pack()

bottom = Frame(win7)
bottom.pack(side= BOTTOM)
label = Label(bottom,text="Project by Keshav Verma").pack()

win7.mainloop() 