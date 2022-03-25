from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import re
import mysql.connector

def mainpage():
    if usercheck.get()=='' or passcheck.get()=='':
        messagebox.showerror('ERROR','Email-id and Password both the field are mandatory')
    
    else:
        conn=mysql.connector.connect(host='localhost',username='root',password='aniket',database='budget_tracker')
        my_cursur = conn.cursor() 
        my_cursur.execute('select * from bt_registration where email_id=%s and password=%s',(
                                                                                            usercheck.get(),
                                                                                            passcheck.get()
                                                                                            ))
        row = my_cursur.fetchone()
        if row==None:
            messagebox.showerror('ERROR','Invalid Email-id and password')
        else:
            open_main = messagebox.askyesno('permission',f'Access to {usercheck.get()}')
            if open_main>0:
                root.destroy()
                from main_window import main_program
                main_program()
            else:
                if not open_main:
                    return
        conn.commit()
        conn.close()
def signup():
    root.destroy()
    from register import registration_form
    registration_form()

def forget(): 
    if usercheck.get()=='':
        messagebox.showerror('ERROR','Please enter Email-Id')

    else:    #while using database add valid email into usercheck
        conn=mysql.connector.connect(host='localhost',username='root',password='aniket',database='budget_tracker')
        my_cursur = conn.cursor() 
        query=('select * from bt_registration where email_id=%s')
        value=(usercheck.get(),)
        my_cursur.execute(query,value)
        row = my_cursur.fetchone()

        if row==None:
            messagebox.showerror('ERROR','Please enter valid Email-id',parent=root)
        else:
            root.destroy()
            from forgetpassword import forget
            forget()
    
def first_page():
    global root
    global usercheck
    global passcheck
    root=Tk()
    root.title('SIGNIN PAGE')
    root.geometry('1270x630+0+0')
    root.config(bg='light grey')
    # root.resizable(0,0)
    root.iconbitmap('moneyicon.ico')


    img=Image.open('main_image.jpg')
    window_bg=ImageTk.PhotoImage(img)

    lbl = Label(root,image=window_bg)
    lbl.place(x=0,y=0)

    money_manager_label=Label(root,text='BUDGET TRACKER',font=('Monaco',35,'bold'),bg='#939395',fg='#0b046b').pack(pady=5)
    
    usercheck = StringVar()
    username=Label(root,text='EMAIL-ID:',font=('Monaco',15,'bold'),bg='light grey').place(x=650,y=150)
    user_name_entry=Entry(root,width=23,font=('Monaco',15),textvariable=usercheck).place(x=780,y=150)
    
    passcheck = StringVar()
    password=Label(root,text='PASSWORD:',font=('Monaco',15,'bold'),bg='light grey').place(x=650,y=220)
    password_entry=Entry(root,width=23,font=('Monaco',15),show='*',textvariable=passcheck).place(x=780,y=220)

    forget_password=Button(root,text='forgot password?',font=('Monaco',15,'bold'),bg='light green',fg='#0b046b',activebackground='light green',command=forget).place(x=800,y=270)
    
    label_account=Label(root,text="don't have an account?",font=('Monaco',15,'bold'),bg='#b89669',fg='#0b046b').place(x=800,y=330)
    
    login=Button(root,text='LOGIN',font=('Monaco',15,'bold'),bg='light green',fg='#0b046b',activebackground='light green',command=mainpage).place(x=800,y=370)
    sing_up=Button(root,text='SIGN UP',font=('Monaco',15,'bold'),bg='light green',fg='#0b046b',activebackground='light green',command=signup).place(x=900,y=370)

    root.mainloop()