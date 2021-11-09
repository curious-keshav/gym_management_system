from tkinter import *
from tkinter import messagebox

from code_db_customer import Database1
db = Database1('dbcustomer1.db')

#/////////////////////////////////////////////////////////////////////////////////////////////////////////

def populate_list():
    name_list.delete(0, END)
    for row in db.fetch():
        name_list.insert(END, row)

#/////////////////////////////////////////////////////////////////////////////////////////////////////////

def add_item():
    if name_text.get() == '' or phone_number_text.get() == '' or joining_text.get() == '' or BMI_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(name_text.get(), phone_number_text.get(),
              joining_text.get(), BMI_text.get())
    name_list.delete(0, END)
    name_list.insert(END, (name_text.get(), phone_number_text.get(),
                            joining_text.get(), BMI_text.get()))
    clear_text()
    populate_list()

#///////////////////////////////////////////////////////////////////////////////////////////////////////////

def select_item(event):
    try:
        global selected_item
        index = name_list.curselection()[0]
        selected_item = name_list.get(index)

        name_entry.delete(0, END)
        name_entry.insert(END, selected_item[1])
        phone_number_entry.delete(0, END)
        phone_number_entry.insert(END, selected_item[2])
        joining_entry.delete(0, END)
        joining_entry.insert(END, selected_item[3])
        BMI_entry.delete(0, END)
        BMI_entry.insert(END, selected_item[4])
    except IndexError:
        pass

#///////////////////////////////////////////////////////////////////////////////////////////////////////////

def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()

#///////////////////////////////////////////////////////////////////////////////////////////////////////////

def update_item():
    db.update(selected_item[0], name_text.get(), phone_number_text.get(), joining_text.get(), BMI_text.get())
    populate_list()

#///////////////////////////////////////////////////////////////////////////////////////////////////////////

def clear_text():
    name_entry.delete(0, END)
    phone_number_entry.delete(0, END)
    joining_entry.delete(0, END)
    BMI_entry.delete(0, END)

#///////////////////////////////////////////////////////////////////////////////////////////////////////////

app = Tk()

app.title("GYM Management System")
app.iconbitmap('icon.ico')
app.maxsize(width= 1100,height = 770)
app.minsize(width= 1100,height = 770)
app.config(bg="black")

topheader = Frame(app)
topheader.pack()
label = Label(topheader,text="GYM Management System").pack()

bg = PhotoImage(file = 'image_customer.png')
label = Label(app,image=bg).pack()

bottom = Frame(app)
bottom.pack(side= BOTTOM)
label = Label(bottom,text="Project by Keshav Verma").pack()

#///////////////////////////////////////////////////////////////////////////////////////////////////////////

name_text = StringVar()
name_label = Label(app, text='Customer Name', font=("calibre",15,"normal"),bd=5)
name_label.place(x=150,y=320)
name_entry = Entry(app, textvariable=name_text,font=("calibre",15,"normal"),bd=5)
name_entry.place(x= 300 ,y =320)

#///////////////////////////////////////////////////////////////////////////////////////////////////////////

phone_number_text = StringVar()
phone_number_label = Label(app, text='Phone Number', font=("calibre",15,"normal"),bd=5)
phone_number_label.place(x = 590 , y =320)
phone_number_entry = Entry(app, textvariable=phone_number_text,font=("calibre",15,"normal"),bd=5)
phone_number_entry.place(x = 730 , y =320)

#///////////////////////////////////////////////////////////////////////////////////////////////////////////

joining_text = StringVar()
joining_label = Label(app, text='Date of Joining ', font=("calibre",15,"normal"),bd=5)
joining_label.place(x = 150 , y=380)
joining_entry = Entry(app, textvariable=joining_text,font=("calibre",15,"normal"),bd =5)
joining_entry.place(x = 300 , y=380)

#///////////////////////////////////////////////////////////////////////////////////////////////////////////

BMI_text = StringVar()
BMI_label = Label(app, text='Customer BMI', font=("calibre",15,"normal"),bd=5)
BMI_label.place(x = 590 , y =380)
BMI_entry = Entry(app, textvariable=BMI_text,font=("calibre",15,"normal"),bd=5)
BMI_entry.place(x = 730,y = 380)

#///////////////////////////////////////////////////////////////////////////////////////////////////////////

name_list = Listbox(app, height=14, width=60, border=0,font=("calibre",12,"normal"),bd=5,bg="silver")
name_list.place(x = 285 , y = 440)

#///////////////////////////////////////////////////////////////////////////////////////////////////////////

scrollbar = Scrollbar(app)
scrollbar.place(x = 813 , y = 448)

#///////////////////////////////////////////////////////////////////////////////////////////////////////////

name_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=name_list.yview)
name_list.bind('<<ListboxSelect>>', select_item)

#///////////////////////////////////////////////////////////////////////////////////////////////////////////

add_btn = Button(app, text='Add', width=12, command=add_item,font=("calibre",12,"normal"),bd=5)
add_btn.place(x = 95 , y = 500)

#///////////////////////////////////////////////////////////////////////////////////////////////////////////

remove_btn = Button(app, text='Remove', width=12, command=remove_item,font=("calibre",12,"normal"),bd=5)
remove_btn.place(x = 95 , y = 600)

#///////////////////////////////////////////////////////////////////////////////////////////////////////////

update_btn = Button(app, text='Update', width=12, command=update_item,font=("calibre",12,"normal"),bd=5)
update_btn.place(x = 900 , y = 500)

#///////////////////////////////////////////////////////////////////////////////////////////////////////////

clear_btn = Button(app, text='Reset', width=12, command=clear_text,font=("calibre",12,"normal"),bd=5)
clear_btn.place(x = 900 , y = 600)

#///////////////////////////////////////////////////////////////////////////////////////////////////////////

app.title('GYM Management System')

populate_list()

app.mainloop()

#///////////////////////////////////////////////////////////////////////////////////////////////////////////