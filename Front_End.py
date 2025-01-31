from tkinter import *

import backend

def get_selected_row(event):
    try:
        global selected_tuple
        index= list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1_v.delete(0,END)
        e1_v.insert(END,selected_tuple[1])
        e2_v.delete(0,END)
        e2_v.insert(END,selected_tuple[2])
        e3_v.delete(0,END)
        e3_v.insert(END,selected_tuple[3])
        e4_v.delete(0,END)
        e4_v.insert(END,selected_tuple[4])
    except IndexError:
        pass

def view_command():
    list1.delete(0,END)
    for items in backend.view():
        list1.insert(END,items)

def search_command():
    list1.delete(0,END)
    for items in backend.search(Title_text.get(),Author_text.get(),Year_text.get(),ISBN_text.get()):
        list1.insert(END,items)
        print(items)


def add_command():
    backend.insert(Title_text.get(),Author_text.get(),Year_text.get(),ISBN_text.get())
    list1.delete(0,END)
    list1.insert(END,(Title_text.get(),Author_text.get(),Year_text.get(),ISBN_text.get()))

def delete_command():
    backend.delete(selected_tuple[0])
    

def update_command():
    backend.update(selected_tuple[0],Title_text.get(),Author_text.get(),Year_text.get(),ISBN_text.get())
    # print(selected_tuple[0],selected_tuple[1],selected_tuple[2],selected_tuple[3],selected_tuple[4])
    

backend.view()


window = Tk()
window.wm_title('BookStore')


e1_t = Label(window, text="Title")
e1_t.grid(row=0, column=0)

Title_text = StringVar()
# Create an Entry widget for user input, linked to e2_value
e1_v= Entry(window, textvariable=Title_text)
e1_v.grid(row=0, column=1)

""" Second box """
e2_t = Label(window, text="Author")
e2_t.grid(row=0, column=2)

Author_text = StringVar()
# Create an Entry widget for user input, linked to e2_value
e2_v= Entry(window, textvariable=Author_text)
e2_v.grid(row=0, column=3)

""" Third box """
e3_t = Label(window, text="Year")
e3_t.grid(row=1, column=0)

Year_text = StringVar()
# Create an Entry widget for user input, linked to e2_value
e3_v= Entry(window, textvariable=Year_text)
e3_v.grid(row=1, column=1)
""" Fourth box """
e4_t = Label(window, text="ISBN")
e4_t.grid(row=1, column=2)

ISBN_text = StringVar()
# Create an Entry widget for user input, linked to e2_value
e4_v= Entry(window, textvariable=ISBN_text)
e4_v.grid(row=1, column=3)


""" Buttons """
b1= Button(window,text='View all',width=12,command= view_command)
b1.grid(row=2,column=3)

b2= Button(window,text="Search Entery",width=12, command=search_command)
b2.grid(row=3,column=3)

b3 = Button(window,text="Add entery",width=12,command=add_command)
b3.grid(row=4,column=3)

b4 = Button(window,text="Update",width=12,command=update_command)
b4.grid(row=5,column=3)

b5 = Button(window,text="Delete",width=12,command=delete_command)
b5.grid(row=6,column=3)

b6= Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=7,column=3)


sb1 =Scrollbar(window)
sb1.grid(row=3,column=2)



""" List Box"""

list1= Listbox(window,)
list1.grid(row=2,column=0, rowspan=6,columnspan=2)

""" Configure the scroll bar with list box"""
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

window.mainloop()