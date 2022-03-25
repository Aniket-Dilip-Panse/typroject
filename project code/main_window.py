from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkcalendar import dateentry
from tkinter import messagebox
import mysql.connector
import login_page
from tkcalendar import Calendar
from datetime import datetime

conn=mysql.connector.connect(host='localhost',username='root',password='aniket',database='budget_tracker')
my_cursur = conn.cursor()

def new():
    amount_credited_entry.delete(0,END)
    amount_debited_entry.delete(0,END)
    total_balance_entry.delete(0,END)
    for item in my_tree.get_children():
        my_tree.delete(item)
    for item2 in my_tree2.get_children():
        my_tree2.delete(item2)

def trackmonthly():
    main_window.destroy()
    from trackmonthly import track_monthly
    track_monthly()   

def tracktransaction():
    main_window.destroy()
    from tracktransaction import track
    track()

def del_credit_transaction():
    # main_window.destroy()
    # from delete_tranaction import del_transaction
    # del_transaction()
    x = my_tree.selection()
    for record in x:
        my_tree.delete(record)
    conn=mysql.connector.connect(host='localhost',username='root',password='aniket',database='budget_tracker')
    my_cursur = conn.cursor()
    query='delete from bt_credit_details where credit_id= email_id=%s'
    value=(login_page.usercheck.get())
    my_cursur.execute(query,value)
    conn.commit()
    conn.close()
    messagebox.showinfo('DELETE','YOUR SELECTED DATA IS DELETED')
    

def del_debit_transaction():
    x = my_tree2.selection()
    for record in x:
        my_tree2.delete(record)

def display_credit():
    conn=mysql.connector.connect(host='localhost',username='root',password='aniket',database='budget_tracker')
    my_cursur = conn.cursor()
    query='select credit_date,amt_credited,mode_credit from bt_credit_details where email_id=%s'
    value=(login_page.usercheck.get(),)
    my_cursur.execute(query,value)
    row=my_cursur.fetchall()
    for ro in row:
        my_tree.insert(parent='',index='end',text='',values=(ro[0],ro[1],ro[2]))

def display_debit():
    conn=mysql.connector.connect(host='localhost',username='root',password='aniket',database='budget_tracker')
    my_cursur = conn.cursor()
    query='select debit_date,money_spend,amt_debited,mode_debit from bt_debit_details where email=%s'
    value=(login_page.usercheck.get(),)
    my_cursur.execute(query,value)
    row=my_cursur.fetchall()
    for ro in row:
        my_tree2.insert(parent='',index='end',text='',values=(ro[0],ro[1],ro[2],ro[3]))


def edit():
    main_window.destroy()
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
    global creditamount
    global debitamount
    global amount_credited_entry
    global amount_debited_entry
    global total_balance_entry
    global my_tree
    global my_tree2

    main_window=Tk()
    main_window.title(' BUDGET TRACKER')
    main_window.geometry('1283x630+0+0')
    # main_window.resizable(0,0)
    main_window.config(bg='#385569')
    main_window.iconbitmap('moneyicon.ico')

    creditamount = StringVar()
    debitamount = StringVar()
    tempdate = StringVar()
    balance = StringVar()
    
    
    menubar=Menu(main_window)
# menubar of mainpage--------------------------------
    profile_menu=Menu(menubar,tearoff=0)
    profile_menu.add_command(label='Profile Edit',command=edit)
    profile_menu.add_command(label='Logout',command=logout)
    menubar.add_cascade(label='Profile',menu=profile_menu)


    file_menu=Menu(menubar,tearoff=0)
    file_menu.add_cascade(label='New Transaction',command=new)
    file_menu.add_command(label='Delete Credit Transaction',command=del_credit_transaction)
    file_menu.add_command(label='Delete Debit Transaction',command=del_debit_transaction)
    file_menu.add_command(label='Display Credit Transaction',command=display_credit)
    file_menu.add_command(label='Display Debit Transaction',command=display_debit)
    menubar.add_cascade(label='File',menu=file_menu)

    history_menu=Menu(menubar,tearoff=0)
    history_menu.add_command(label='Track Transaction',command=tracktransaction)
    history_menu.add_command(label='Track Monthly',command=trackmonthly)
    menubar.add_cascade(label='History',menu=history_menu)
    main_window.config(menu=menubar)

# first frame of mainpage------------------------------------
    expenditure_frame=Frame(main_window,width=500,height=325,highlightbackground='light grey',bg='light grey',bd=3,relief=RAISED).place(x=10,y=10)

    expenditure_label=Label(expenditure_frame,text='Expenditure Info',font=('Monaco',20,'bold'),fg='#385569',bg='light grey').place(x=115,y=11)

    date_label=Label(expenditure_frame,text='Date              :',font=('Monaco',15,'bold'),fg='#385569',bg='light grey').place(x=25,y=50)

    date_label_entry=DateEntry(expenditure_frame,selectmode='none',width=20,textvariable=tempdate).place(x=255,y=50)


    amount_credited=Label(expenditure_frame,text='Amount Credited   :',font=('Monaco',15,'bold'),fg='#385569',bg='light grey').place(x=25,y=80)

    amount_credited_entry=Entry(expenditure_frame,width=20,font=('Monaco',15,'bold'),textvariable=creditamount)
    amount_credited_entry.place(x=255,y=80)

    mode_credit_label=Label(expenditure_frame,text='Mode Of Credit    :',font=('Monaco',15,'bold'),fg='#385569',bg='light grey').place(x=25,y=120)

    mode_of_credit=['Cash','Debit Card','Net Banking','UPI','Cash','Other']
    creditoption=StringVar(expenditure_frame)

    security_question_entry=ttk.OptionMenu(expenditure_frame,creditoption,*mode_of_credit).place(x=255,y=120)

    money_spend_label=Label(expenditure_frame,text='Money Spend On    :',font=('Monaco',15,'bold'),fg='#385569',bg='light grey').place(x=25,y=160)   

    money_spend_on=['EMI','Maintainence','Shopping','Food','Health','Entertainment','Travelling','EMI','Other']
    moneyspendclick=StringVar(expenditure_frame)
    money_spend_on_entry=ttk.OptionMenu(expenditure_frame,moneyspendclick,*money_spend_on).place(x=255,y=160)

    amount_debited=Label(expenditure_frame,text='Amount Debited    :',font=('Monaco',15,'bold'),fg='#385569',bg='light grey').place(x=25,y=190)

    amount_debited_entry=Entry(expenditure_frame,width=20,font=('Monaco',15,'bold'),textvariable=debitamount)
    amount_debited_entry.place(x=255,y=190)

    mode_debit_label=Label(expenditure_frame,text='Mode Of Debit     :',font=('Monaco',15,'bold'),fg='#385569',bg='light grey').place(x=25,y=230)


    mode_debit_list=['Cash','Debit Card','Net Banking','UPI','Cash','Other']
    modedebitclick=StringVar(expenditure_frame)
    mode_debit_entry=ttk.OptionMenu(expenditure_frame,modedebitclick,*mode_debit_list).place(x=255,y=230)
    
# Second frame of mainpage------------------------------------

    total_frame=Frame(main_window,width=500,height=255,highlightbackground='light grey',bg='light grey',bd=3,relief=RAISED).place(x=10,y=350)

    total_label=Label(expenditure_frame,text='Total Details',font=('Monaco',20,'bold'),fg='#385569',bg='light grey').place(x=130,y=358)

    total_balance=Label(expenditure_frame,text='Total balance:',font=('Monaco',15,'bold'),fg='#385569',bg='light grey').place(x=25,y=425)
    
    total_balance_entry=Entry(expenditure_frame,width=20,font=('Monaco',15,'bold'),textvariable='balance')
    total_balance_entry.place(x=195,y=425)
    
    def Show():
        conn=mysql.connector.connect(host='localhost',username='root',password='aniket',database='budget_tracker')
        my_cursur = conn.cursor()
        query1='set @total_credit= (select sum(amt_credited) from budget_tracker.bt_credit_details where email_id=%s);'
        query2='set @total_debit = (select sum(amt_debited) from budget_tracker.bt_debit_details where email=%s);'
        query3='select (@total_credit-@total_debit) as remaining_money;'
        value1=(login_page.usercheck.get(),)
        value2=(login_page.usercheck.get(),)
        exe1=my_cursur.execute(query1,value1)
        exe2=my_cursur.execute(query2,value2)
        exe3=my_cursur.execute(query3)
        row=my_cursur.fetchone()
        if row==None:
            messagebox.showerror('ERROR','NO DATA FOUND')
        else:
            total_balance_entry.insert(0,row)
    show_button=Button(expenditure_frame,text='SHOW',font=('Monaco',15,'bold'),fg='#385569',bd=3,command=Show).place(x=200,y=490)
 


# Third frame of mainpage------------------------------------
    frame=Frame(main_window, bg='light grey',bd=5,relief=RAISED,width=730,height=595)
    frame.place(x=530,y=10)
    
    credit_details=LabelFrame(frame, text="Credit Details",width=720,height=590)  
    credit_details.place(x=10,y=5)  

# add some style
    style=ttk.Style()
# pick a theme to apply all the configure changes
    style.theme_use("clam")
# configure our treeview
    style.configure("Treeview",background='light grey',foreground='#385569',rowheight=25,fieldbackground='light grey')
    my_tree = ttk.Treeview(credit_details)
    # defining column
    my_tree['columns']=('DATE','Amount Credited','Mode Of Credit')
    # formating column
    my_tree.column("#0",width=0,stretch=NO)
    my_tree.column("DATE",anchor=CENTER,width=220,minwidth=160)
    my_tree.column("Amount Credited",anchor=CENTER,width=220,minwidth=200)
    my_tree.column('Mode Of Credit',anchor=CENTER,width=235,minwidth=160)
    # create heading 
    my_tree.heading('#0',text='',anchor=W)
    my_tree.heading("DATE",text='DATE',anchor=CENTER)
    my_tree.heading('Amount Credited',text="Amount Credited",anchor=CENTER)
    my_tree.heading('Mode Of Credit',text='Mode Of Credit',anchor=CENTER)

    treeScroll = ttk.Scrollbar(credit_details)
    treeScroll.configure(command=my_tree.yview)
    my_tree.configure(yscrollcommand=treeScroll.set)
    treeScroll.pack(side= RIGHT, fill= BOTH)

    my_tree.pack()

    debit_details=LabelFrame(main_window,text='Debit Details')
    debit_details.place(x=540,y=330)

    # add some style
    style=ttk.Style()
# pick a theme to apply all the configure changes
    style.theme_use("clam")
# configure our treeview
    style.configure("Treeview",background='light grey',foreground='#385569',rowheight=20,fieldbackground='light grey')
    my_tree2 = ttk.Treeview(debit_details)
    # defining column
    my_tree2['columns']=('DATE','Expenditure','Amount debited','Mode')
    # formating column
    my_tree2.column("#0",width=0,stretch=NO)
    my_tree2.column("DATE",anchor=CENTER,width=165,minwidth=130)
    my_tree2.column("Expenditure",anchor=CENTER,width=165,minwidth=150)
    my_tree2.column('Amount debited',anchor=CENTER,width=175,minwidth=140)
    my_tree2.column('Mode',anchor=CENTER,width=173,minwidth=100)
    # create heading 
    my_tree2.heading('#0',text='',anchor=W)
    my_tree2.heading("DATE",text='DATE',anchor=CENTER)
    my_tree2.heading('Expenditure',text='Expenditure',anchor=CENTER)
    my_tree2.heading('Amount debited',text="Amount Debited",anchor=CENTER)
    my_tree2.heading('Mode',text='Mode Of Debit',anchor=CENTER)

    treeScroll = ttk.Scrollbar(debit_details)
    treeScroll.configure(command=my_tree2.yview)
    my_tree2.configure(yscrollcommand=treeScroll.set)
    treeScroll.pack(side= RIGHT, fill= BOTH)

    my_tree2.pack()


    def checkamtcredit(creditamount):
        if creditamount.isdigit():
            return True
        if creditamount=='':
            return True
        else:
            messagebox.showerror('Invalid','Not Allowed\nOnly Number')
            return False

    def checkamtdebit(debitamount):
        if debitamount.isdigit():
            return True
        if debitamount=='':
            return True
        else:
            messagebox.showerror('Invalid','Not Allowed\nOnly Number')
            return False
    
    def cleardata():
        total_balance_entry.delete(0,END)

    def credit_validation(): 
        if creditamount.get()=='':
            messagebox.showerror('ERROR','Please Enter Your Credit Amount',parent=main_window)
            amount_credited_entry.focus()
        else:
            tep_date = list(tempdate.get().split('/'))
            leng=len(tep_date)
            key=tep_date[2]
            for i in range(leng-2,-1,-1):
                tep_date[i+1]=tep_date[i]
            tep_date[0]=key
            org_date='/'.join(tep_date)
            print(tempdate.get())
            print(org_date)
            print(tep_date)

            my_tree.insert(parent='',index=0,text='',values=(org_date,amount_credited_entry.get(),creditoption.get()))
            conn=mysql.connector.connect(host='localhost',username='root',password='aniket',database='budget_tracker')
            my_cursur = conn.cursor()
            my_cursur.execute('insert into bt_credit_details(credit_date,amt_credited,mode_credit,email_id) values(%s,%s,%s,%s)',(org_date,creditamount.get(),creditoption.get(),login_page.usercheck.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo('SUCCESS','YOUR DATA IS REC0RDED DONE')
            amount_credited_entry.delete(0,END)
            
    def debit_validation():
        if debitamount.get()=='':
            messagebox.showerror('ERROR','Please Enter Your Debit Amount',parent=main_window)
            amount_debited_entry.focus()
        else:
            tep_date = list(tempdate.get().split('/'))
            leng=len(tep_date)
            key=tep_date[2]
            for i in range(leng-2,-1,-1):
                tep_date[i+1]=tep_date[i]
            tep_date[0]=key
            org_date='/'.join(tep_date)
            my_tree2.insert(parent='',index=0,text='',values=(org_date,moneyspendclick.get(),amount_debited_entry.get(),modedebitclick.get()))
            conn=mysql.connector.connect(host='localhost',username='root',password='aniket',database='budget_tracker')
            my_cursur = conn.cursor()
            my_cursur.execute('insert into bt_debit_details (debit_date,money_spend,amt_debited,mode_debit,email) values(%s,%s,%s,%s,%s)',(org_date,moneyspendclick.get(),debitamount.get(),modedebitclick.get(),login_page.usercheck.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo('SUCCESS','YOUR DATA IS RECRDED DONE')
            amount_debited_entry.delete(0,END)
        
    validate_credit = main_window.register(checkamtcredit)
    amount_credited_entry.config(validate='key',validatecommand=(validate_credit,'%P'))

    validate_debit = main_window.register(checkamtdebit)
    amount_debited_entry.config(validate='key',validatecommand=(validate_credit,'%P'))

    clear_button=Button(expenditure_frame,text='CLEAR',font=('Monaco',15,'bold'),fg='#385569',bd=3,command=cleardata)
    clear_button.place(x=300,y=490)

    add_credit_button=Button(expenditure_frame,text='Add Credit Details',font=('Monaco',15,'bold'),fg='#385569',bd=3,command=credit_validation).place(x=25,y=280)

    add_debit_button=Button(expenditure_frame,text='Add Debit Details',font=('Monaco',15,'bold'),fg='#385569',bd=3,command=debit_validation).place(x=265,y=280)


    main_window.mainloop()