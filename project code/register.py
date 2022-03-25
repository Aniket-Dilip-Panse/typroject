from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from validate_email import validate_email
from password_validation import PasswordPolicy
import mysql.connector

def submit():
    registration_window.destroy()
    from login_page import first_page
    first_page()

def back():
    registration_window.destroy()
    from login_page import first_page
    first_page()

def registration_form():
    global registration_window
    global name
    global lastname
    global contact
    global emailid
    global options_var
    global answer
    global setpasswd
    registration_window=Tk()
    registration_window.title('REGISTRATION')
    # registration_window.resizable(0,0)
    registration_window.geometry('1270x630+0+0')
    registration_window.config(bg='#385569')
    registration_window.iconbitmap('moneyicon.ico')


    # background register image
    img = Image.open('register_background.jpg')
    register_bg = ImageTk.PhotoImage(img)

    register_image_label = Label(registration_window,image=register_bg)
    register_image_label.place(x=250,y=0,relwidth=1,relheight=1)

    left = Image.open('left.png')
    left = ImageTk.PhotoImage(left)

    left_image_label=Label(registration_window,image=left)
    left_image_label.place(x=80,y=50,width=400,height=500)


    name = StringVar()
    lastname = StringVar()
    contact = StringVar()
    emailid = StringVar()
    options_var = StringVar()
    answer = StringVar()
    setpasswd = StringVar()
    confirmpasswd = StringVar()

    # ===============register frame====================
    frame=Frame(registration_window,bg='white')
    frame.place(x=480,y=50,width=700,height=500)

    register_here=Label(frame,text='REGISTER HERE',font=('Monaco',20,'bold'),bg='white',fg='#0b046b')
    register_here.place(x=50,y=30)

    first_name=Label(frame,text='First Name',font=('Monaco',15,'bold'),bg='white',fg='#0b046b')
    first_name.place(x=50,y=100)

    first_name_entry=Entry(frame,font=('Monaco',15),bg='lightgray',textvariable=name)
    first_name_entry.place(x=50,y=130,width=250)

    last_name=Label(frame,text='Last Name',font=('Monaco',15,'bold'),bg='white',fg='#0b046b')
    last_name.place(x=370,y=100)

    last_name_entry=Entry(frame,font=('Monaco',15),bg='lightgray',textvariable=lastname)
    last_name_entry.place(x=370,y=130,width=250)
# row3=============================================
    contact_number=Label(frame,text='Contact NO.',font=('Monaco',15,'bold'),bg='white',fg='#0b046b')
    contact_number.place(x=50,y=170)

    contact_number_entry=Entry(frame,font=('Monaco',15),bg='lightgray',textvariable=contact)
    contact_number_entry.place(x=50,y=200,width=250)


    email=Label(frame,text='Email-ID',font=('Monaco',15,'bold'),bg='white',fg='#0b046b')
    email.place(x=370,y=170)

    email_entry=Entry(frame,font=('Monaco',15),bg='lightgray',textvariable=emailid)
    email_entry.place(x=370,y=200,width=300)



# row3==================================================
    security_question=Label(frame,text='Security Question',font=('Monaco',15,'bold'),bg='white',fg='#0b046b')
    security_question.place(x=50,y=240)

    optionlist=['YOUR NICK NAME','YOUR BIRTH PLACE','YOUR FAVOURITE FOOD','YOUR DREAM PLACE NAME','YOUR NICK NAME']
    clickedoption=StringVar(frame,options_var)
    options_var.set('YOUR NICK NAME')
    security_question_entry=ttk.OptionMenu(frame,clickedoption,*optionlist).place(x=50,y=280)

    security_answer=Label(frame,text='Security Answer',font=('Monaco',15,'bold'),bg='white',fg='#0b046b')
    security_answer.place(x=370,y=240)

    security_answer_entry=Entry(frame,font=('Monaco',15),bg='lightgray',textvariable=answer)
    security_answer_entry.place(x=370,y=280,width=250)

# row 4==================================
    set_password=Label(frame,text='Set Password',font=('Monaco',15,'bold'),bg='white',fg='#0b046b')
    set_password.place(x=50,y=320) 

    set_password_entry=Entry(frame,font=('Monaco',15),bg='lightgray',show='*',textvariable=setpasswd)
    set_password_entry.place(x=50,y=360,width=250)  

    confirm_password=Label(frame,text='Confirm Password',font=('Monaco',15,'bold'),bg='white',fg='#0b046b')
    confirm_password.place(x=370,y=320)

    confirm_password_entry=Entry(frame,font=('Monaco',15),bg='lightgray',show='*',textvariable=confirmpasswd)
    confirm_password_entry.place(x=370,y=360,width=250)

    back_button=Button(registration_window,text='←',font=('Monaco',20,'bold'),bg='#00e8ff',fg='#0b046b',activebackground='#16a9db',command=back)
    back_button.place(x=0,y=0)

    def checkfirstname(name):
        if name=='':
            return True
        if name.isalpha():
            return True
        else:
            messagebox.showerror('Invalid','Not Accepted\nOnly Alphabet\nExample:- aniket')
            return False
    
    def checklastname(lastname):
        if lastname=='':
            return True
        if lastname.isalpha():
            return True
        else:
            messagebox.showerror('Invalid','Not Accepted\nOnly Alphabet\nExample:- panse')
            return False

    def checkcontact(contact):
        if contact.isdigit():
            return True
        if len(str(contact))==0:
            return True
        else:
            messagebox.showerror('Invalid','Not Accepted\nOnly Number\nExample:- 8249537610')
            return False
    
    def checkemail(emailid):
        global is_valid
        is_valid=validate_email(emailid,verify=True)
        if is_valid:
            messagebox.showinfo('Valid','Email is valid')
            return True
        else:
            messagebox.showerror('Valid','Email is not valid\nExample:-aniket13@gmail.com')
            return False
                        
    def checkanswer(answer):
        if answer=='':
            return True
        if answer.isalnum() or not(answer.isidentifier()):
            return True
        else:
            messagebox.showerror('Invalid','Not Accepted\nOnly Alphabet and number\nExample:-soku143')
            return False

    def checksetpassword(setpasswd):
        global is_valid_password
        global checkpasswd
        is_valid_password = PasswordPolicy()
        checkpasswd = is_valid_password.validate(setpasswd)
        if checkpasswd:
            messagebox.showinfo('Valid','Set Password is Valid')
            return True
        else:
            messagebox.showerror('Invalid','Set Password is Not Valid\nminimum 8 character\nmaximum 100 character\nhas uppercase Letter\nhas lowercase Letter\nhas atleast one digit\nhas no spaces')
            return False

    def checkconfirmpassword(confirmpasswd):
        if confirmpasswd=='':
            return True
        else:
            return False

    def validation():
        if name.get()=='':
            messagebox.showerror('invalid','Please Enter Your First name',parent=registration_window)
            first_name_entry.focus()

        elif lastname.get()=='':
            messagebox.showerror('invalid','Please Enter Your Last name',parent=registration_window)
            last_name_entry.focus()

        elif contact.get()=='' or len(contact.get())!=10:
            messagebox.showerror('invalid','Please Check Your Contact Number',parent=registration_window)
            contact_number_entry.focus()

        elif emailid.get()=='':
            messagebox.showerror('invalid','Please Enter your Email-Id',parent=registration_window)
            email_entry.focus()

        elif answer.get()=='':
            messagebox.showerror('invalid','Please Enter Your Security Answer',parent=registration_window)

        elif setpasswd.get()=='':
            messagebox.showerror('invalid','Please Enter Your Password',parent=registration_window)

        elif confirmpasswd.get()=='':
            messagebox.showerror('invalid','Please Enter Your Confirm Password',parent=registration_window)

        elif setpasswd.get()!=confirmpasswd.get():
            messagebox.showerror('invalid','Password and Confirm Password must be same',parent=registration_window)

        # database adding after this..........................
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='aniket',database='budget_tracker')
                my_cursur = conn.cursor()
                query=('select * from bt_registration where email_id=%s')
                value=(emailid.get(),)
                my_cursur.execute(query,value)
                row=my_cursur.fetchone()
                if row!=None:
                    messagebox.showerror('ERROR','user already exists\nPlease try another email',parent=registration_window)
                else:
                    my_cursur.execute('insert into bt_registration values(%s,%s,%s,%s,%s,%s,%s)',(name.get(),
                                                                                                 lastname.get(),
                                                                                                 contact.get(),
                                                                                                 emailid.get(),
                                                                                                 options_var.get(),
                                                                                                 answer.get(),
                                                                                                 setpasswd.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo('Sucessfully','YOUR REGISTRATION IS COMPLETED\nPLEASE LOGIN',parent=registration_window)
                first_name_entry.delete(0,END)
                last_name_entry.delete(0,END)
                contact_number_entry.delete(0,END)
                email_entry.delete(0,END)
                security_answer_entry.delete(0,END)
                set_password_entry.delete(0,END)
                confirm_password_entry.delete(0,END)

            except Exception as es:
                messagebox.showerror('ERROR',f'Due to {str(es)}',parent=registration_window)


    validatefirstname=registration_window.register(checkfirstname)
    first_name_entry.config(validate='key',validatecommand=(validatefirstname,'%P'))

    validatelastname=registration_window.register(checklastname)
    last_name_entry.config(validate='key',validatecommand=(validatelastname,'%P'))

    validatecontact=registration_window.register(checkcontact)
    contact_number_entry.config(validate='key',validatecommand=(validatecontact,'%P'))
    
    validateemail=registration_window.register(checkemail)
    email_entry.config(validate='focusout',validatecommand=(validateemail,'%P'))

    validateanswer=registration_window.register(checkanswer)
    security_answer_entry.config(validate='focusout',validatecommand=(validateanswer,'%P'))

    validatesetpassword=registration_window.register(checksetpassword)
    set_password_entry.config(validate='focusout',validatecommand=(validatesetpassword,'%P'))

    validateconfirmpassword=registration_window.register(checkconfirmpassword)
    confirm_password_entry.config(validate='focusout',validatecommand=(validateconfirmpassword,'%P'))

    submit_button=Button(frame,text='Submit',font=('Monaco',15,'bold'),bg='#00e8ff',fg='#0b046b',activebackground='#16a9db',command=validation)
    submit_button.place(x=290,y=420)

    registration_window.mainloop()