from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from password_validation import PasswordPolicy
import mysql.connector
import login_page
def submit():
    forget_password_window.destroy()
    from login_page import first_page
    first_page()

def back():
    forget_password_window.destroy()
    from login_page import first_page
    first_page()

def stop_forget_window():
    forget_password_window.destroy()

def forget():
    global forget_bg
    global forget_password_window
    global setpaswd
    global confirmpasswd
    global answer
    forget_password_window=Tk()
    forget_password_window.title('Forget Password')
    forget_password_window.geometry('1240x630+0+0')
    forget_password_window.config(bg='#5cd4f7')
    # forget_password_window.resizable(0,0)
    forget_password_window.iconbitmap('moneyicon.ico')


    forget_password_label=Label(forget_password_window,text='FORGET PASSWORD',font=('Monaco',35,'bold'),bg='#5cd4f7',fg='#044b83').pack(fill=BOTH)

    info_label=Label(forget_password_window,text=''' During Registration\nIf you choose a Security Question\nas your NICK NAME then select the\nNICK NAME option and provide the\nsame answer....''',font=('Monaco',15,'bold'),bg='#5cd4f7',fg='#044b83').place(x=13,y=200)

    setpaswd = StringVar()
    confirmpasswd = StringVar()
    answer = StringVar()


    frame=Frame(forget_password_window,bg='white')
    frame.place(x=450,y=100,width=700,height=400)

    register_here=Label(frame,text='SET NEW PASSWORD',font=('Monaco',20,'bold'),bg='white',fg='#0b046b')
    register_here.place(x=50,y=50)

    security_question=Label(frame,text='Security Question',font=('Monaco',15,'bold'),bg='white',fg='#0b046b')
    security_question.place(x=50,y=120)

    optionlist=['YOUR NICK NAME','YOUR BIRTH PLACE' ,'YOUR FAVOURITE FOOD','YOUR PET NAME','YOUR NICK NAME']
    clickedoption=StringVar(frame)
    security_question_entry=ttk.OptionMenu(frame,clickedoption,*optionlist).place(x=50,y=150)

    security_answer=Label(frame,text='Security Answer',font=('Monaco',15,'bold'),bg='white',fg='#0b046b')
    security_answer.place(x=370,y=120)

    security_answer_entry=Entry(frame,font=('Monaco',15),bg='lightgray',textvariable=answer)
    security_answer_entry.place(x=370,y=150,width=250)


# row3=============================================
    set_new_password=Label(frame,text='Set New Password',font=('Monaco',15,'bold'),bg='white',fg='#0b046b')
    set_new_password.place(x=50,y=190)

    set_new_password_entry=Entry(frame,font=('Monaco',15),bg='lightgray',show='*',textvariable=setpaswd)
    set_new_password_entry.place(x=50,y=220,width=250)

    confirm_new_password=Label(frame,text='Confirm New Password',font=('Monaco',15,'bold'),bg='white',fg='#0b046b')
    confirm_new_password.place(x=370,y=190)

    confirm_new_password_entry=Entry(frame,font=('Monaco',15),bg='lightgray',show='*',textvariable=confirmpasswd)
    confirm_new_password_entry.place(x=370,y=220,width=250)

    def checksetpassword(setpasswd):
        global is_valid_password
        global checkpasswd
        is_valid_password = PasswordPolicy()
        checkpasswd = is_valid_password.validate(setpasswd)
        if checkpasswd:
            messagebox.showinfo('Valid','Set New Password is Valid')
            return True
        else:
            messagebox.showerror('Invalid','Set New Password is Not Valid\nminimum 8 character\nmaximum 100 character\nhas uppercase Letter\nhas lowercase Letter\nhas atleast one digit\nhas no spaces')
            return False

    def checkconfirmpassword(confirmpasswd):
        if confirmpasswd=='':
            return True
        else:
            return False

    def checkanswer(answer):
        if answer=='':
            return True
        if answer.isalnum() or not(answer.isidentifier()):
            return True
        else:
            messagebox.showerror('Invalid','Not Accepted\nOnly Alphabet and number\nExample:-soku143')
            return False

    def validation():
        if answer.get()=='':
            messagebox.showerror('invalid','Please Enter Your Security Answer',parent=forget_password_window)
        elif setpaswd.get()=='':
            messagebox.showerror('invalid','Please Enter Your New Password',parent=forget_password_window)
        elif confirmpasswd.get()=='':
            messagebox.showerror('invalid','Please Enter Your New Confirm Password',parent=forget_password_window)
        elif setpaswd.get()!=confirmpasswd.get():
            messagebox.showerror('invalid','Password and Confirm Password must be same',parent=forget_password_window)
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='aniket',database='budget_tracker')
            my_cursur = conn.cursor() 
            query = ('select * from bt_registration where email_id=%s and security_question=%s and security_answer=%s')
            value=(login_page.usercheck.get(),clickedoption.get(),answer.get(),)
            my_cursur.execute(query,value)
            row = my_cursur.fetchone()

            if row == None:
                messagebox.showerror('ERROR','please select correct security question and enter correct answer')
            else:
                query=('update bt_registration set password=%s where email_id=%s')
                value=(setpaswd.get(),login_page.usercheck.get())
                my_cursur.execute(query,value)
                conn.commit()
                conn.close()
                messagebox.showinfo('SUCCESS','you have reset your password\nplease try to login with new password')
                security_answer_entry.delete(0,END)
                set_new_password_entry.delete(0,END)
                confirm_new_password_entry.delete(0,END)

    validatesetnewpassword=forget_password_window.register(checksetpassword)
    set_new_password_entry.config(validate='focusout',validatecommand=(validatesetnewpassword,'%P'))

    validateconfirmnewpassword=forget_password_window.register(checkconfirmpassword)
    confirm_new_password_entry.config(validate='focusout',validatecommand=(validateconfirmnewpassword,'%P'))

    validateanswer=forget_password_window.register(checkanswer)
    security_answer_entry.config(validate='focusout',validatecommand=(validateanswer,'%P'))

    save_button=Button(frame,text='Save',font=('Monaco',15,'bold'),bg='#00e8ff',fg='#0b046b',activebackground='#16a9db',command=validation)
    save_button.place(x=290,y=320)

    back_button=Button(forget_password_window,text='←',font=('Monaco',20,'bold'),bg='#00e8ff',fg='#0b046b',activebackground='#16a9db',command=back)
    back_button.place(x=0,y=0)