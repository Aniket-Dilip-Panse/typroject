from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk

def mainpage():
    root.destroy()
    from main_window import main_program
    main_program()

def signup():
    root.destroy()
    from register import registration
    registration()


def forget():
    from forgetpassword import forget
    forget()

def first_page():
    global root
    root=Tk()
    root.title('SIGNIN PAGE')
    root.geometry('1022x630+10+10')
    root.config(bg='light grey')
    # root.resizable(0,0)
    root.iconbitmap('moneyicon.ico')
    

    img=Image.open('money.jpg')
    window_bg=ImageTk.PhotoImage(img)

    lbl = Label(root,image=window_bg)
    lbl.place(x=0,y=0)


    money_manager_label=Label(root,text='BUDGET TRACKER',font=('Monaco',35,'bold'),bg='light grey',fg='#0b046b').pack()

    username=Label(root,text='EMAIL-ID:',font=('Monaco',15,'bold'),bg='light grey').place(x=600,y=150)
    user_name_entry=ttk.Entry(root,width=23,font=('Monaco',15)).place(x=730,y=150)

    password=Label(root,text='PASSWORD:',font=('Monaco',15,'bold'),bg='light grey').place(x=600,y=220)
    password_entry=ttk.Entry(root,width=23,font=('Monaco',15),show='*').place(x=730,y=220)

    forget_password=Button(root,text='forget password?',font=('Monaco',15,'bold'),bg='#16a9db',fg='#0b046b',activebackground='#16a9db',command=forget).place(x=630,y=270)
    
    label_account=Label(root,text="don't have an account?",font=('Monaco',15,'bold'),bg='white',fg='#3ec7f6').place(x=630,y=330)
    
    login=Button(root,text='LOGIN',font=('Monaco',15,'bold'),bg='#16a9db',fg='#0b046b',activebackground='#16a9db',command=mainpage).place(x=630,y=370)
    sing_up=Button(root,text='SIGN UP',font=('Monaco',15,'bold'),bg='#16a9db',fg='#0b046b',activebackground='#16a9db',command=signup).place(x=750,y=370)
    
    root.mainloop()        