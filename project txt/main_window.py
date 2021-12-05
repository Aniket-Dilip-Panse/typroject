from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkcalendar import dateentry


def edit():
    from profile_edit import profileedit
    profileedit()
    
def logout():
    main_window.destroy()
    from login_page import first_page
    first_page()

def new_window():
    new=Toplevel(root)


def main_program():
    global main_window
    main_window=Tk()
    main_window.title('BUDGET TRACKER')
    main_window.geometry('1253x630+10+10')
    # main_window.resizable(0,0)
    main_window.config(bg='#385569')
    main_window.iconbitmap('moneyicon.ico')

    menubar=Menu(main_window)
# menubar of mainpage--------------------------------
    profile_menu=Menu(menubar,tearoff=0)
    profile_menu.add_command(label='Profile Edit',command=edit)
    profile_menu.add_command(label='Logout',command=logout)
    menubar.add_cascade(label='Profile',menu=profile_menu)

    file_menu=Menu(menubar,tearoff=0)
    file_menu.add_command(label='New Transaction')
    file_menu.add_command(label='Delete Transaction')
    file_menu.add_command(label='Display Credit Transaction')
    file_menu.add_command(label='Display Debit Transaction')
    file_menu.add_command(label='view Last Transaction')
    menubar.add_cascade(label='File',menu=file_menu)

    history_menu=Menu(menubar,tearoff=0)
    history_menu.add_command(label='Track Transaction')
    history_menu.add_command(label='Track Monthly')
    menubar.add_cascade(label='History',menu=history_menu)
    main_window.config(menu=menubar)

# first frame of mainpage------------------------------------
    expenditure_frame=Frame(main_window,width=500,height=325,highlightbackground='light grey',bg='light grey',bd=3,relief=RAISED).place(x=10,y=10)

    expenditure_label=Label(expenditure_frame,text='Expenditure Info',font=('Monaco',20,'bold'),fg='#385569',bg='light grey').place(x=115,y=11)

    date_label=Label(expenditure_frame,text='Date              :',font=('Monaco',15,'bold'),fg='#385569',bg='light grey').place(x=25,y=50)

    date=DateEntry(expenditure_frame,selectmode='day',width=20).place(x=255,y=50)

    amount_credited=Label(expenditure_frame,text='Amount Credited   :',font=('Monaco',15,'bold'),fg='#385569',bg='light grey').place(x=25,y=80)

    amount_credited_entry=Entry(expenditure_frame,width=20,font=('Monaco',15,'bold')).place(x=255,y=80)

    mode_credit_label=Label(expenditure_frame,text='Mode Of Credit    :',font=('Monaco',15,'bold'),fg='#385569',bg='light grey').place(x=25,y=120)

    mode_of_credit=['Cash','Debit Card','Net Banking','UPI','Cash','Other']
    creditoption=StringVar(expenditure_frame)
    security_question_entry=ttk.OptionMenu(expenditure_frame,creditoption,*mode_of_credit).place(x=255,y=120)

    money_spend_label=Label(expenditure_frame,text='Money Spend On    :',font=('Monaco',15,'bold'),fg='#385569',bg='light grey').place(x=25,y=160)   

    money_spend_on=['EMI','Maintainence','Shopping','Food','Health','Entertainment','Travelling','EMI','Other']
    moneyspendclick=StringVar(expenditure_frame)
    money_spend_on_entry=ttk.OptionMenu(expenditure_frame,moneyspendclick,*money_spend_on).place(x=255,y=160)

    amount_debited=Label(expenditure_frame,text='Amount Debited    :',font=('Monaco',15,'bold'),fg='#385569',bg='light grey').place(x=25,y=190)

    amount_debited_entry=Entry(expenditure_frame,width=20,font=('Monaco',15,'bold')).place(x=255,y=190)

    mode_debit_label=Label(expenditure_frame,text='Mode Of Debit     :',font=('Monaco',15,'bold'),fg='#385569',bg='light grey').place(x=25,y=230)


    mode_debit_list=['Cash','Debit Card','Net Banking','UPI','Cash','Other']
    modedebitclick=StringVar(expenditure_frame)
    mode_debit_entry=ttk.OptionMenu(expenditure_frame,modedebitclick,*mode_debit_list).place(x=255,y=230)

    add_credit_button=Button(expenditure_frame,text='Add Credit Details',font=('Monaco',15,'bold'),fg='#385569',bd=3).place(x=25,y=280)
    
    add_debit_button=Button(expenditure_frame,text='Add Debit Details',font=('Monaco',15,'bold'),fg='#385569',bd=3).place(x=265,y=280)

# Second frame of mainpage------------------------------------

    total_frame=Frame(main_window,width=500,height=243,highlightbackground='light grey',bg='light grey',bd=3,relief=RAISED).place(x=10,y=350)

    total_label=Label(expenditure_frame,text='Total Details',font=('Monaco',20,'bold'),fg='#385569',bg='light grey').place(x=130,y=358)

    total_balance=Label(expenditure_frame,text='Total balance:',font=('Monaco',15,'bold'),fg='#385569',bg='light grey').place(x=25,y=425)

    total_balance_entry=Entry(expenditure_frame,width=20,font=('Monaco',15,'bold')).place(x=195,y=425)

    show_button=Button(expenditure_frame,text='SHOW',font=('Monaco',15,'bold'),fg='#385569',bd=3).place(x=200,y=490)
    
    clear_button=Button(expenditure_frame,text='CLEAR',font=('Monaco',15,'bold'),fg='#385569',bd=3).place(x=300,y=490)

# Third frame of mainpage------------------------------------    
    frame=Frame(main_window, bg='light grey',bd=5,relief=RAISED,width=700,height=585)
    frame.place(x=530,y=10)
    
    credit_details=LabelFrame(frame, text="Credit Details")  
    credit_details.place(x=10,y=5)  

    credit_date=Label(credit_details,text='date').place(x=10,y=0)
    credit_amount=Label(credit_details,text='Amount Credited').place(x=260,y=0)
    credit_mode=Label(credit_details,text='Mode Of Credit').place(x=550,y=0)
    
    listbox=Listbox(credit_details,width=109,height=14).pack(pady=20)
  


    debit_details=LabelFrame(main_window,text='Debit Details')
    debit_details.place(x=540,y=330)

    debit_date=Label(debit_details,text='date').place(x=10,y=5)
    debit_expenditure=Label(debit_details,text='Expenditure').place(x=150,y=5)
    debit_amount=Label(debit_details,text='Amount Debited').place(x=330,y=5)
    debit_mode=Label(debit_details,text='Mode Of Payment').pack(anchor=NE)


    listbox=Listbox(debit_details,width=109,height=13).pack()