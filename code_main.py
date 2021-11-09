
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import os

#/////////////////////////////////////////////////////////////////////////////////////////////////

win = Tk()
win.title("GYM Management System")
win.iconbitmap('icon.ico')
win.maxsize(width= 1100,height = 770)
win.minsize(width= 1100,height = 720)
# win.config(bg="yellow")

#/////////////////////////////////////////////////////////////////////////////////////////////////

topheader = Frame(win)
topheader.pack()
label = Label(topheader,text="GYM Management System").pack()

bg = PhotoImage(file = 'image_main.png')
label = Label(win,image=bg).pack()

bottom = Frame(win)
bottom.pack(side= BOTTOM)
label = Label(bottom,text="Project by Keshav Verma").pack()

#//////////////////////////////////////////////////////////////////////////////////////////////////     

def sel():
    if var.get() == 1:
      os.system("code_customer_setting")
    elif var.get() == 2:
      os.system("code_package_setting")
    elif var.get() == 3:
      os.system("code_customer_setting")
    elif var.get() == 4:
      os.system("code_package_setting")
    elif var.get() == 5:
      os.system("code_customer_setting")
    elif var.get() == 6:
      os.system("code_package_setting")
    elif var.get() == 7:
      os.system("code_aboutus")

#//////////////////////////////////////////////////////////////////////////////////////////////////

def refresh():
    var.set(0)
    win.update()

#//////////////////////////////////////////////////////////////////////////////////////////////////

var = IntVar()
R1 = Radiobutton(win,variable=var,text = "Add Customer",font=("calibre",15,"normal"),bg="black",fg="white", value=1,bd=5,selectcolor='black')
R1.place(x = 450,y = 275)
R2 = Radiobutton(win, variable=var,text = "Add Package",font=("calibre",15,"normal"),bg="black",fg="white", value=2,bd=5,selectcolor='black')
R2.place(x = 450,y = 325)
R3 = Radiobutton(win, variable=var,text = "Show all Customers",font=("calibre",15,"normal"),bg="black",fg="white", value=3,bd=5,selectcolor='black')
R3.place(x = 450,y = 375)
R4 = Radiobutton(win, variable=var,text = "Show all Packages",font=("calibre",15,"normal"),bg="black",fg="white", value=4,bd=5,selectcolor='black')
R4.place(x = 450,y = 425)
R5 = Radiobutton(win, variable=var,text = "Remove Customer",font=("calibre",15,"normal"),bg="black",fg="white", value=5,bd=5,selectcolor='black')
R5.place(x = 450,y = 475)
R6 = Radiobutton(win,variable=var, text = "Remove Package",font= ("calibre",15,"normal"), bg="black",fg="white",value=6,bd=5,selectcolor='black')
R6.place(x = 450,y = 525)
R7 = Radiobutton(win,variable=var, text = "About us",font= ("calibre",15,"normal"), bg="black",fg="white",value=7,bd=5,selectcolor='black')
R7.place(x = 450,y = 575)
label = Label(win)
label.pack()

#//////////////////////////////////////////////////////////////////////////////////////////////////

btn1 = Button(win,text ="Enter",font=("calibre",12,"normal"),bg="green",fg="white",command=sel)
btn1.place(x=475,y=650)

btn2 = Button(win,text ="Reset",font=("calibre",12,"normal"),bg="brown",fg="white",command=refresh)
btn2.place(x=575,y=650)

#//////////////////////////////////////////////////////////////////////////////////////////////////

win.mainloop() 

#//////////////////////////////////////////////////////////////////////////////////////////////////