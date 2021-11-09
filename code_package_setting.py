from tkinter import *
from tkinter import messagebox

from code_db_package import Database2
db = Database2('dbpackage1.db')

#//////////////////////////////////////////////////////////////////////////////////////////

def populate_list():
    type_list.delete(0, END)
    for row in db.fetch():
        type_list.insert(END, row)

#/////////////////////////////////////////////////////////////////////////////////////////

def add_item():
    if type_text.get() == '' or facility_text.get() == '' or cost_text.get() == '': 
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(type_text.get(), facility_text.get(),
              cost_text.get())
    type_list.delete(0, END)
    type_list.insert(END, (type_text.get(), facility_text.get(),
                            cost_text.get() ))
    clear_text()
    populate_list()

#//////////////////////////////////////////////////////////////////////////////////////////

def select_item(event):
    try:
        global selected_item
        index = type_list.curselection()[0]
        selected_item = type_list.get(index)

        type_entry.delete(0, END)
        type_entry.insert(END, selected_item[1])
        facility_entry.delete(0, END)
        facility_entry.insert(END, selected_item[2])
        cost_entry.delete(0, END)
        cost_entry.insert(END, selected_item[3])
    except IndexError:
        pass

#//////////////////////////////////////////////////////////////////////////////////////////

def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()

#//////////////////////////////////////////////////////////////////////////////////////////

def update_item():
    db.update(selected_item[0], type_text.get(), facility_text.get(), cost_text.get())
    populate_list()

#///////////////////////////////////////////////////////////////////////////////////////////

def clear_text():
    type_entry.delete(0, END)
    facility_entry.delete(0, END)
    cost_entry.delete(0, END)

#///////////////////////////////////////////////////////////////////////////////////////////

app1 = Tk()

app1.title("GYM Management System")
app1.iconbitmap('icon.ico')
app1.maxsize(width= 1100,height = 770)
app1.minsize(width= 1100,height = 770)
app1.config(bg="black")

topheader = Frame(app1)
topheader.pack()
label = Label(topheader,text="GYM Management System").pack()

bg = PhotoImage(file = 'image_package.png')
label = Label(app1,image=bg).pack()

bottom = Frame(app1)
bottom.pack(side= BOTTOM)
label = Label(bottom,text="Project by Keshav Verma").pack()

#//////////////////////////////////////////////////////////////////////////////////////////

type_text = StringVar()
type_label = Label(app1, text=' Package Type ', font=("calibre",15,"normal"),bd=5)
type_label.place(x=150,y=320)
type_entry = Entry(app1, textvariable=type_text,font=("calibre",15,"normal"),bd=5)
type_entry.place(x= 300 ,y =320)

#///////////////////////////////////////////////////////////////////////////////////////////

facility_text = StringVar()
facility_label = Label(app1, text=' Pack Facility ', font=("calibre",15,"normal"),bd=5)
facility_label.place(x = 590 , y =320)
facility_entry = Entry(app1, textvariable=facility_text,font=("calibre",15,"normal"),bd=5)
facility_entry.place(x = 725 , y =320)

#///////////////////////////////////////////////////////////////////////////////////////////////////

cost_text = StringVar()
cost_label = Label(app1, text=' Package Cost ', font=("calibre",15,"normal"),bd=5)
cost_label.place(x = 370 , y=380)
cost_entry = Entry(app1, textvariable=cost_text,font=("calibre",15,"normal"),bd =5)
cost_entry.place(x = 520 , y=380)

#////////////////////////////////////////////////////////////////////////////////////////////////////

type_list = Listbox(app1, height=14, width=60, border=0,font=("calibre",12,"normal"),bd=5,bg="silver")
type_list.place(x = 285 , y = 440)

#/////////////////////////////////////////////////////////////////////////////////////////////////////

scrollbar = Scrollbar(app1)
scrollbar.place(x = 813 , y = 448)

#/////////////////////////////////////////////////////////////////////////////////////////////////////

type_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=type_list.yview)
type_list.bind('<<ListboxSelect>>', select_item)

#//////////////////////////////////////////////////////////////////////////////////////////////////////

add_btn = Button(app1, text='Add', width=12, command=add_item,font=("calibre",12,"normal"),bd=5)
add_btn.place(x = 95 , y = 500)

#////////////////////////////////////////////////////////////////////////////////////////////////////////

remove_btn = Button(app1, text='Remove', width=12, command=remove_item,font=("calibre",12,"normal"),bd=5)
remove_btn.place(x = 95 , y = 600)

#//////////////////////////////////////////////////////////////////////////////////////////////////////////

update_btn = Button(app1, text='Update', width=12, command=update_item,font=("calibre",12,"normal"),bd=5)
update_btn.place(x = 900 , y = 500)

#//////////////////////////////////////////////////////////////////////////////////////////////////////////

clear_btn = Button(app1, text='Reset', width=12, command=clear_text,font=("calibre",12,"normal"),bd=5)
clear_btn.place(x = 900 , y = 600)

#/////////////////////////////////////////////////////////////////////////////////////////////////////////
app1.title('GYM Management System')

populate_list()

app1.mainloop()

#//////////////////////////////////////////////////////////////////////////////////////////////////////////