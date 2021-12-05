from tkinter import *
from tkinter import ttk

def update():
    profile_edit.destroy()

def back():
    profile_edit.destroy()


def profileedit():
    global profile_edit
    profile_edit=Tk()
    profile_edit.title('REGISTRATION')
    profile_edit.geometry('550x500+10+10')
    profile_edit.resizable(0,0)
    profile_edit.config(bg='#385569')
    profile_edit.iconbitmap('moneyicon.ico')

    personal_label=Label(profile_edit,text='Personal Data',font=('Monaco',40,'bold'),bg='#385569',fg='#3ec7f6').pack()

    first_name=Label(profile_edit,text='First Name:',font=('Monaco',15,'bold'),bg='#385569',fg='#05e6f9').place(x=100,y=100)
    first_name_entry=ttk.Entry(profile_edit,font=('Monaco',15,'bold'),).place(x=300,y=100)


    last_name=Label(profile_edit,text='Last Name:',font=('Monaco',15,'bold'),bg='#385569',fg='#05e6f9').place(x=100,y=150)
    last_name_entry=ttk.Entry(profile_edit,font=('Monaco',15,'bold')).place(x=300,y=150)


    occupation=Label(profile_edit,text='occupation:',font=('Monaco',15,'bold'),bg='#385569',fg='#05e6f9').place(x=100,y=200)
    occupation_entry=ttk.Entry(profile_edit,font=('Monaco',15,'bold')).place(x=300,y=200)



    mobile_number=Label(profile_edit,text='Mobile Number:',font=('Monaco',15,'bold'),bg='#385569',fg='#05e6f9').place(x=100,y=250)
    mobile_number_entry=ttk.Entry(profile_edit,font=('Monaco',15,'bold')).place(x=300,y=250)

    
    email=Label(profile_edit,text='Email-ID:',font=('Monaco',15,'bold'),bg='#385569',fg='#05e6f9').place(x=100,y=300)
    email_entry=ttk.Entry(profile_edit,font=('Monaco',15,'bold')).place(x=300,y=300)

    update_button=Button(profile_edit,text='Update',font=('Monaco',15,'bold'),bg='#16a9db',fg='#0b046b',activebackground='#16a9db',command=update).place(x=200,y=350)

    back_button=Button(profile_edit,text='<-',font=('Monaco',20,'bold'),bg='#16a9db',fg='#0b046b',activebackground='#16a9db',command=back).place(x=0,y=0)

