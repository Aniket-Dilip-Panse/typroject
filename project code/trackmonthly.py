#Import tkinter package
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
import mysql.connector
import login_page
from matplotlib import pyplot as plt
import numpy as np
from tkinter import messagebox

def VIEW():
    conn = mysql.connector.connect(
        host='localhost', user='root', password='aniket', database='budget_tracker')
    my_cursur = conn.cursor()
    a=month1_list.index(monthoption.get())
    b=month2_list.index(monthoption2.get())
    if a==0 or b==0:
        messagebox.showerror('invalid','Please Select Month1 AND Month2 For Graph')
    else:
        query1="select sum(amt_credited) as month1 from bt_credit_details where email_id=%s and credit_date like '%-_%s-%';"
        value1=(login_page.usercheck.get(),a)
        my_cursur.execute(query1,value1)
        row1=my_cursur.fetchone()

        query2="select sum(amt_debited) as month2 from bt_debit_details where email=%s and debit_date like '%-_%s-%';"
        value2=(login_page.usercheck.get(),a)
        my_cursur.execute(query2,value2)
        row2=my_cursur.fetchone()

        query3="select sum(amt_credited) as month1 from bt_credit_details where email_id=%s and credit_date like '%-_%s-%';"
        value3=(login_page.usercheck.get(),b)
        my_cursur.execute(query3,value3)
        row3=my_cursur.fetchone()

        query4="select sum(amt_debited) as month2 from bt_debit_details where email=%s and debit_date like '%-_%s-%';"
        value4=(login_page.usercheck.get(),b)
        my_cursur.execute(query4,value4)
        row4=my_cursur.fetchone()
    
        w=0.4
        x=[monthoption.get(),monthoption2.get()]
        credit=[]
        debit=[]
        for i in row1:
            credit.append(int(i))
            for j in row3:
                credit.append(int(j))
        for k in row2:
            debit.append(int(k))
            for l in row4:
                debit.append(int(l))
        print(credit)
        print(debit)
        fontdict2 = {'family': 'Monaco',
        'color':  'darkred',
        'weight': 'normal',
        'size': 15,
        }

        fontdict3 = {'family': 'Monaco',
        'color':  'darkred',
        'weight': 'normal',
        'size': 20,
        }

        bar1=np.arange(len(x))
        bar2=[m+w for m in bar1]

        plt.bar(bar1,credit,w,label='credit')
        plt.bar(bar2,debit,w,label="debit")
        plt.xlabel("Month",fontdict=fontdict2)
        plt.ylabel("Total Credit & Debit",fontdict=fontdict2)
        plt.title("AMOUNT V/S MONTH",fontdict=fontdict3)   
        plt.xticks(bar1+w/2,x) 
        plt.legend()
        plt.show()
    

def back():
    track_monthly.destroy()
    from main_window import main_program
    main_program()

def CLEAR():
    month1_entry.delete(0,END)
    credited_amount_entry1.delete(0,END)
    credited_amount_entry2.delete(0,END)
    debited_amount_entry1.delete(0,END)
    debited_amount_entry2.delete(0,END)

def COMPARE():
    conn = mysql.connector.connect(
        host='localhost', user='root', password='aniket', database='budget_tracker')
    my_cursur = conn.cursor()
    x=month1_list.index(monthoption.get())
    y=month2_list.index(monthoption2.get())
    query1="select sum(amt_credited) as month1 from bt_credit_details where email_id=%s and credit_date like '%-_%s-%';"
    value1=(login_page.usercheck.get(),x)
    my_cursur.execute(query1,value1)
    row1=my_cursur.fetchone()
    entry3.set(row1)

    query2="select sum(amt_credited) as month2 from bt_credit_details where email_id=%s and credit_date like '%-_%s-%';"
    value2=(login_page.usercheck.get(),y)
    my_cursur.execute(query2,value2)
    row2=my_cursur.fetchone()
    entry2.set(row2)

    query3="select sum(amt_debited) as month1 from bt_debit_details where email=%s and debit_date like '%-_%s-%';"
    value3=(login_page.usercheck.get(),x)
    my_cursur.execute(query3,value3)
    row3=my_cursur.fetchone()
    entry5.set(row3)

    query4="select sum(amt_debited) as month2 from bt_debit_details where email=%s and debit_date like '%-_%s-%';"
    value4=(login_page.usercheck.get(),y)
    my_cursur.execute(query4,value4)
    row4=my_cursur.fetchone()
    entry4.set(row4)

def track_monthly():
    global track_monthly
    global month1_entry
    global month1_list
    global month2_list
    global credited_amount_entry1
    global credited_amount_entry2
    global debited_amount_entry1
    global debited_amount_entry2
    global monthoption
    global monthoption2
    global entry1
    global entry2
    global entry3
    global entry4
    global entry5

    track_monthly = Tk()
    # track_monthly.resizable(0,0)
    track_monthly.geometry('1250x600+10+10')
    track_monthly.title('TRACK MONTHLY')
    track_monthly.iconbitmap('moneyicon.ico')
    track_monthly.config(bg='#385569')

    entry1 =StringVar()
    entry2 =StringVar()
    entry3 =StringVar()
    entry4 =StringVar()
    entry5 =StringVar()

    back_button=Button(track_monthly,text='←',font=('Monaco',15,'bold'),bg='#16a9db',fg='#0b046b',activebackground='#16a9db',command=back).pack(anchor=NW)

    # LabelFrame is created
    labelframe =LabelFrame(track_monthly, text = 'Compare Monthly',font=('Monaco',15,'bold'),bg='#385569',fg='#3ec7f6')
    labelframe.pack(expand = 'yes', fill = 'both')
# Buttons are defined and created
    month1_list=['Select Month','January','Feburary','March','April','May','June','July','August','September','October','November','December']
    monthoption = StringVar(labelframe)
    month1 = Label(labelframe, text ='Month1',font=('Monaco',15,'bold'),bg='#385569',fg='#3ec7f6')
    month1.place(x = 450, y = 10)
    month1_entry = ttk.OptionMenu(track_monthly,monthoption,*month1_list)
    month1_entry.place(x = 450, y = 100)

    month2_list=['Select Month','January','Feburary','March','April','May','June','July','August','September','October','November','December']
    monthoption2=StringVar()
    month2 = Label(labelframe, text ='Month2     ',font=('Monaco',15,'bold'),bg='#385569',fg='#3ec7f6')
    month2.place(x = 630, y = 10)
    month2_entry =ttk.OptionMenu(track_monthly,monthoption2,*month2_list)
    month2_entry.place(x = 630, y = 100)

    compare_button=Button(labelframe,text='Compare',font=('Monaco',15,'bold'),bg='#16a9db',fg='#0b046b',activebackground='#16a9db',command=COMPARE).place(x=535,y=80)

    month1 = Label(labelframe, text ='Month1',font=('Monaco',15,'bold'),bg='#385569',fg='#3ec7f6')
    month1.place(x = 450, y = 110)
    month1_entry = Entry(labelframe,textvariable=entry1,width=20,font=('Monaco',10,'bold'))
    month1_entry.place(x = 450, y = 150)

    month2 = Label(labelframe, text ='Month2     ',font=('Monaco',15,'bold'),bg='#385569',fg='#3ec7f6')
    month2.place(x = 640, y = 110)

    credited_amount_label=Label(labelframe,text='Credited Amount',font=('Monaco',15,'bold'),bg='#385569',fg='#3ec7f6').place(x=250,y=150)

    credited_amount_entry1 = Entry(labelframe,textvariable=entry2,width=20,font=('Monaco',10,'bold'))
    credited_amount_entry1.place(x = 630, y = 150)

    credited_amount_entry2 = Entry(labelframe,textvariable=entry3,font=('Monaco',10,'bold'),width=20)
    credited_amount_entry2.place(x = 450, y = 150)

    debited_amount_label=Label(labelframe,text='Debited Amount',font=('Monaco',15,'bold'),bg='#385569',fg='#3ec7f6').place(x=250,y=180)

    debited_amount_entry1 = Entry(labelframe,textvariable=entry4,width=20,font=('Monaco',10,'bold'))
    debited_amount_entry1.place(x = 630, y = 180)

    debited_amount_entry2 = Entry(labelframe,textvariable=entry5,width=20,font=('Monaco',10,'bold'))
    debited_amount_entry2.place(x = 450, y = 180)

    clear_button=Button(labelframe,text='Clear',font=('Monaco',15,'bold'),bg='#16a9db',fg='#0b046b',activebackground='#16a9db',command=CLEAR).place(x=550,y=210)

    labelframe =LabelFrame(track_monthly, text = 'Graphical Representation Monthly',font=('Monaco',15,'bold'),bg='#385569',fg='#3ec7f6')
    labelframe.pack(expand = 'yes', fill = 'both')

    plot = Label(labelframe, text ='Plot:',font=('Monaco',15,'bold'),bg='#385569',fg='#3ec7f6')
    plot.place(x = 430, y = 10)

    plotlist=['bar chart',]
    clickedoption=StringVar(labelframe)
    security_question_entry=ttk.OptionMenu(labelframe,clickedoption,*plotlist).place(x=500,y=10)

    view_button=Button(labelframe,text='Monthly Histroy',font=('Monaco',20,'bold'),bg='#16a9db',fg='#0b046b',activebackground='#16a9db',command=VIEW).place(x=500,y=70)

    track_monthly.mainloop()
