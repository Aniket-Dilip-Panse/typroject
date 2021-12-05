from tkinter import *
from tkinter import ttk

def stop_forget_window():
    forget_password_window.destroy()



def forget():
    global forget_password_window
    forget_password_window=Tk()
    forget_password_window.title('Forget Password')
    forget_password_window.geometry('590x630+10+10')
    forget_password_window.resizable(0,0)
    forget_password_window.config(bg='#385569')
    forget_password_window.iconbitmap('moneyicon.ico')
    
    forget_password_label=Label(forget_password_window,text='FORGET PASSWORD',font=('Monaco',35,'bold'),bg='#385569',fg='#3ec7f6').pack(pady=15)

    security_question=Label(forget_password_window,text='Security Question',font=('Monaco',15,'bold'),bg='#385569',fg='#05e6f9').pack(pady=10)

    optionlist=['YOUR NICK NAME','YOUR BIRTH','YOUR FAVOURITE FOOD','YOUR PET NAME']
    clickedoption=StringVar(forget_password_window)
    security_question_entry=ttk.OptionMenu(forget_password_window,clickedoption,*optionlist).pack(pady=10)

    security_answer=Label(forget_password_window,text='Security Answer',font=('Monaco',15,'bold'),bg='#385569',fg='#05e6f9').pack(pady=10)

    security_answer_entry=ttk.Entry(forget_password_window,width=15,font=('Monaco',15,'bold')).pack(pady=7)

    new_password=Label(forget_password_window,text='New Password',font=('Monaco',15,'bold'),bg='#385569',fg='#05e6f9').pack(pady=10)

    new_password_entry=ttk.Entry(forget_password_window,width=15,font=('Monaco',15,'bold')).pack(pady=7)

    confirm_password=Label(forget_password_window,text='Confirm New Password',font=('Monaco',15,'bold'),bg='#385569',fg='#05e6f9').pack(pady=10)

    confirm_password_entry=ttk.Entry(forget_password_window,width=15,font=('Monaco',15,'bold')).pack(pady=7)

    reset_password=Button(forget_password_window,text='Reset Password',font=('Monaco',20,'bold'),bg='#16a9db',fg='#0b046b',activebackground='#16a9db',command=stop_forget_window).pack(pady=20)
