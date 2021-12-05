from tkinter import *
from tkinter import ttk

def submit():
    registration_window.destroy()
    from login_page import first_page
    first_page()

def back():
    registration_window.destroy()
    from login_page import first_page
    first_page()

def registration():
    global registration_window
    registration_window=Tk()
    registration_window.title('REGISTRATION')
    registration_window.geometry('1022x630+10+10')
    # registration_window.resizable(0,0)
    registration_window.config(bg='#385569')
    registration_window.iconbitmap('moneyicon.ico')

    user_details_label=Label(registration_window,text='USER DETAILS',font=('Monaco',40,'bold'),bg='#385569',fg='#3ec7f6').pack()

    first_name=Label(registration_window,text='First Name',font=('Monaco',15,'bold'),bg='#385569',fg='#05e6f9').place(x=100,y=85)

    first_name_entry=ttk.Entry(registration_window,width=15,font=('Monaco',15,'bold')).place(x=100,y=120)

    last_name=Label(registration_window,text='Last Name',font=('Monaco',15,'bold'),bg='#385569',fg='#05e6f9').place(x=400,y=85)

    last_name_entry=ttk.Entry(registration_window,width=15,font=('Monaco',15,'bold')).place(x=400,y=120)

    Email_id=Label(registration_window,text='Email-ID',font=('Monaco',15,'bold'),bg='#385569',fg='#05e6f9').place(x=700,y=85)

    Email_id_entry=ttk.Entry(registration_window,width=25,font=('Monaco',15,'bold')).place(x=700,y=120)

    occupation=Label(registration_window,text='Ocuupation',font=('Monaco',15,'bold'),bg='#385569',fg='#05e6f9').place(x=275,y=185)

    occupation_entry=ttk.Entry(registration_window,width=15,font=('Monaco',15,'bold')).place(x=275,y=225)

    mobile_number=Label(registration_window,text='Mobile Number',font=('Monaco',15,'bold'),bg='#385569',fg='#05e6f9').place(x=600,y=185)

    mobile_number_entry=ttk.Entry(registration_window,width=15,font=('Monaco',15,'bold')).place(x=600,y=225)

    security_question=Label(registration_window,text='Security Question',font=('Monaco',15,'bold'),bg='#385569',fg='#05e6f9').place(x=275,y=300)
    
    optionlist=['YOUR NICK NAME','YOUR BIRTH','YOUR FAVOURITE FOOD','YOUR PET NAME','YOUR NICK NAME']
    clickedoption=StringVar(registration_window)
    security_question_entry=ttk.OptionMenu(registration_window,clickedoption,*optionlist).place(x=275,y=340)

    security_answer=Label(registration_window,text='Security Answer',font=('Monaco',15,'bold'),bg='#385569',fg='#05e6f9').place(x=600,y=300)

    security_answer_entry=ttk.Entry(registration_window,width=15,font=('Monaco',15,'bold')).place(x=600,y=340)

    set_password=Label(registration_window,text='Set Password',font=('Monaco',15,'bold'),bg='#385569',fg='#05e6f9').place(x=275,y=390)

    set_password_entry=ttk.Entry(registration_window,width=15,font=('Monaco',15,'bold')).place(x=275,y=430)
    
    confirm_password=Label(registration_window,text='Confirm Password',font=('Monaco',15,'bold'),bg='#385569',fg='#05e6f9').place(x=600,y=390)

    confirm_password_entry=ttk.Entry(registration_window,width=15,font=('Monaco',15,'bold')).place(x=600,y=430)

    submit_button=Button(registration_window,text='Submit',font=('Monaco',15,'bold'),bg='#16a9db',fg='#0b046b',activebackground='#16a9db',command=submit).place(x=480,y=500)

    back_button=Button(registration_window,text='<-',font=('Monaco',20,'bold'),bg='#16a9db',fg='#0b046b',activebackground='#16a9db',command=back).place(x=0,y=0)
    