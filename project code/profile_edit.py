from tkinter import *
from tkinter import ttk
from tkcalendar import dateentry
from PIL import Image,ImageTk
from tkinter import messagebox
# from validate_email import validate_email
import mysql.connector
import register
import login_page
import register


def submit():
    profile_edit_window.destroy()
    from login_page import first_page
    first_page()

def back():
    profile_edit_window.destroy()
    from main_window import main_program
    main_program()


def profileedit():
    global profile_edit_window
    global name
    global lastname
    global contact
    global emailid
    global options_var
    global answer

    profile_edit_window=Tk()
    # profile_edit_window.resizable(0,0)
    profile_edit_window.title('PROFILE EDIT')
    profile_edit_window.geometry('1270x630+0+0')
    profile_edit_window.iconbitmap('moneyicon.ico')

    img=Image.open('two_color.png')
    window_bg=ImageTk.PhotoImage(img)

    lbl = Label(profile_edit_window,image=window_bg)
    lbl.place(x=0,y=0)

    name = StringVar()
    lastname = StringVar()
    contact = StringVar()
    emailid = StringVar()
    # options_var = StringVar()
    answer = StringVar()

    conn=mysql.connector.connect(host='localhost',username='root',password='aniket',database='budget_tracker')
    my_cursur = conn.cursor()
    query1='select fist_name from bt_registration where email_id = %s'
    value1=(login_page.usercheck.get(),)
    my_cursur.execute(query1,value1)
    row1=my_cursur.fetchone()

    query2='select last_name from bt_registration where email_id = %s'
    value2=(login_page.usercheck.get(),)
    my_cursur.execute(query2,value2)
    row2=my_cursur.fetchone()

    query3='select contact_number from bt_registration where email_id = %s'
    value3=(login_page.usercheck.get(),)
    my_cursur.execute(query3,value3)
    row3=my_cursur.fetchone()

    query4='select security_question from bt_registration where email_id = %s'
    value4=(login_page.usercheck.get(),)
    my_cursur.execute(query4,value4)
    row4=my_cursur.fetchone()

    query5='select security_answer from bt_registration where email_id = %s'
    value5=(login_page.usercheck.get(),)
    my_cursur.execute(query5,value5)
    row5=my_cursur.fetchone()

    frame=Frame(profile_edit_window,bg='white')
    frame.place(x=280,y=50,width=700,height=500)

    register_here=Label(frame,text='PROFILE EDIT',font=('Monaco',20,'bold'),bg='white',fg='#0b046b')
    register_here.place(x=50,y=30)

    first_name=Label(frame,text='First Name',font=('Monaco',15,'bold'),bg='white',fg='#0b046b')
    first_name.place(x=50,y=100)

    first_name_entry=Entry(frame,font=('Monaco',15),bg='lightgray',textvariable=name)
    first_name_entry.place(x=50,y=130,width=250)
    name.set(row1)

    last_name=Label(frame,text='Last Name',font=('Monaco',15,'bold'),bg='white',fg='#0b046b')
    last_name.place(x=370,y=100)

    last_name_entry=Entry(frame,font=('Monaco',15),bg='lightgray',textvariable=lastname)
    last_name_entry.place(x=370,y=130,width=250)
    lastname.set(row2)
# row3=============================================
    contact_number=Label(frame,text='Contact NO.',font=('Monaco',15,'bold'),bg='white',fg='#0b046b')
    contact_number.place(x=50,y=170)

    contact_number_entry=Entry(frame,font=('Monaco',15),bg='lightgray',textvariable=contact)
    contact_number_entry.place(x=50,y=200,width=250)
    contact.set(row3)

    email=Label(frame,text='Email-ID',font=('Monaco',15,'bold'),bg='white',fg='#0b046b')
    email.place(x=370,y=170)

    email_entry=Entry(frame,font=('Monaco',15),bg='lightgray',textvariable=emailid,state=DISABLED)
    emailid.set(login_page.usercheck.get())
    email_entry.place(x=370,y=200,width=320)

# row3==================================================
    security_question=Label(frame,text='Security Question',font=('Monaco',15,'bold'),bg='white',fg='#0b046b')
    security_question.place(x=50,y=240)

    optionlist=['YOUR NICK NAME','YOUR BIRTH PLACE','YOUR FAVOURITE FOOD','YOUR PET ANIMAL NAME','YOUR NICK NAME']
    clickedoption=StringVar(frame)
    security_question_entry=ttk.OptionMenu(frame,clickedoption,*optionlist).place(x=50,y=280)
    clickedoption.set(row4)

    security_answer=Label(frame,text='Security Answer',font=('Monaco',15,'bold'),bg='white',fg='#0b046b')
    security_answer.place(x=370,y=240)

    security_answer_entry=Entry(frame,font=('Monaco',15),bg='lightgray',textvariable=answer)
    security_answer_entry.place(x=370,y=280,width=250)
    answer.set(row5)

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
                        
    def checkanswer(answer):
        if answer=='':
            return True
        if answer.isalnum() or not(answer.isidentifier()):
            return True
        else:
            messagebox.showerror('Invalid','Not Accepted\nOnly Alphabet and number\nExample:-soku143')
            return False

    def validation():
        if name.get()=='':
            messagebox.showerror('invalid','Please Enter Your First name',parent=profile_edit_window)
            first_name_entry.focus()

        elif lastname.get()=='':
            messagebox.showerror('invalid','Please Enter Your Last name',parent=profile_edit_window)
            last_name_entry.focus()

        elif contact.get()=='' or len(contact.get())!=10:
            messagebox.showerror('invalid','Please Check Your Contact Number',parent=profile_edit_window)
            contact_number_entry.focus()

        elif answer.get()=='':
            messagebox.showerror('invalid','Please Enter Your Security Answer',parent=profile_edit_window)
            security_answer_entry.focus()
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='aniket',database='budget_tracker')
            my_cursur = conn.cursor()
            query = ('select * from bt_registration where email_id=%s')
            value = (email_entry.get(),)
            my_cursur.execute(query,value)
            row = my_cursur.fetchone()

            if row == None:
                messagebox.showerror('ERROR','Email-id Not Found\nPlease enter same Email-id you used for Login')
            else:
                query=('update bt_registration set fist_name=%s,last_name=%s,contact_number=%s, security_question=%s,security_answer=%s where email_id=%s')
                value=(name.get(),lastname.get(),contact.get(),clickedoption.get(),answer.get(),emailid.get())
                my_cursur.execute(query,value)
            conn.commit()
            conn.close()
            messagebox.showinfo('SUCCESS','You Have Reset Your Profile.\nUse New Profile Details')

    validatefirstname=profile_edit_window.register(checkfirstname)
    first_name_entry.config(validate='key',validatecommand=(validatefirstname,'%P'))

    validatelastname=profile_edit_window.register(checklastname)
    last_name_entry.config(validate='key',validatecommand=(validatelastname,'%P'))

    validatecontact=profile_edit_window.register(checkcontact)
    contact_number_entry.config(validate='key',validatecommand=(validatecontact,'%P'))
    
    validateanswer=profile_edit_window.register(checkanswer)
    security_answer_entry.config(validate='focusout',validatecommand=(validateanswer,'%P'))

# row 4==================================

    submit_button=Button(frame,text='Submit',font=('Monaco',15,'bold'),bg='#21c3ff',fg='#0b046b',activebackground='#16a9db',command=validation)
    submit_button.place(x=290,y=420)

    back_button=Button(frame,text='←',font=('Monaco',20,'bold'),bg='#21c3ff',fg='#0b046b',activebackground='#16a9db',command=back)
    back_button.place(x=0,y=0)


    profile_edit_window.mainloop()