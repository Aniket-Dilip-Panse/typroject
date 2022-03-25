# Import tkinter package
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
import mysql.connector
import login_page
from main_window import *
import numpy as np
import matplotlib.pyplot as plt
import mysql.connector
# tkinter window is created by defining the geometry


def VIEW():
    conn = mysql.connector.connect(
        host='localhost', user='root', password='aniket', database='budget_tracker')
    my_cursur = conn.cursor()
    query = "select money_spend,amt_debited from bt_debit_details where email=%s"
    Value = (login_page.usercheck.get(),)
    my_cursur.execute(query, Value)
    row = my_cursur.fetchall()

    plt.figure(figsize=(10, 7))
    plt.legend(loc='upper left')
    spendmoney = []
    amtdeb = []

    for i in row:
        spendmoney.append(i[0])
        amtdeb.append(i[1])
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
        if clickedoption.get() == 'Bar Chart':
            plt.bar(spendmoney, amtdeb)
            plt.xlabel("EXPENDITURE",fontdict=fontdict2)
            plt.ylabel("AMOUNT",fontdict=fontdict2)
            plt.title("Debit Amount V/S Expenditure",fontdict=fontdict3)
        # elif clickedoption.get()== 'pie chart':
        #     plt.pie(amtdeb,labels=spendmoney)
    plt.show()

def SHOW():
    conn = mysql.connector.connect(
        host='localhost', username='root', password='aniket', database='budget_tracker')
    my_cursur = conn.cursor()
    tep_date = list(tempdate1.get().split('/'))
    leng = len(tep_date)
    key = tep_date[2]
    for i in range(leng-2, -1, -1):
        tep_date[i+1] = tep_date[i]
    tep_date[0] = key
    org_date1 = '/'.join(tep_date)

    tep_date = list(tempdate2.get().split('/'))
    leng = len(tep_date)
    key = tep_date[2]
    for i in range(leng-2, -1, -1):
        tep_date[i+1] = tep_date[i]
    tep_date[0] = key
    org_date2 = '/'.join(tep_date)

    query1 = "select sum(amt_credited) as compare from bt_credit_details where (credit_date between %s and %s) and (email_id=%s)"
    value1 = (org_date1, org_date2, login_page.usercheck.get())
    my_cursur.execute(query1, value1)
    row1 = my_cursur.fetchone()
    moneyearn.set(row1)

    query2 = "select sum(amt_debited) as compare from bt_debit_details where (debit_date between %s and %s) and (email=%s)"
    value2 = (org_date1, org_date2, login_page.usercheck.get())
    my_cursur.execute(query2, value2)
    row2 = my_cursur.fetchone()
    moneyspend.set(row2)

    query4 = 'set @total_debit = (select sum(amt_credited) from budget_tracker.bt_credit_details where(credit_date between %s and %s) and (email_id=%s));'
    query5 = 'set @total_credit= (select sum(amt_debited) from budget_tracker.bt_debit_details where(debit_date between %s and %s) and (email=%s));'
    query6 = 'select (@total_debit - @total_credit) as remaining_money;'
    value4 = (org_date1, org_date2, login_page.usercheck.get())
    value5 = (org_date1, org_date2, login_page.usercheck.get())
    exe1 = my_cursur.execute(query4, value4)
    exe2 = my_cursur.execute(query5, value5)
    exe3 = my_cursur.execute(query6)
    row3 = my_cursur.fetchone()
    moneyavailabel.set(row3)


def back():
    track_transaction.destroy()
    from main_window import main_program
    main_program()


def CLEAR():
    starting_date_entry.delete(0, END)
    spend_money_entry.delete(0, END)
    money_available_entry.delete(0, END)


def track():
    global track_transaction
    global starting_date_entry
    global spend_money_entry
    global money_available_entry
    global date_entry
    global end_date_entry
    global org_date1
    global org_date2

    global moneyearn
    global moneyspend
    global moneyavailabel
    global tempdate1
    global tempdate2
    global clickedoption

    track_transaction = Tk()
    # track_transaction.resizable(0,0)
    track_transaction.geometry('1250x600+10+10')
    track_transaction.title('TRACK TRANSACTION')
    track_transaction.iconbitmap('moneyicon.ico')
    track_transaction.config(bg='#385569')

    moneyearn = StringVar()
    moneyspend = StringVar()
    moneyavailabel = StringVar()
    tempdate1 = StringVar()
    tempdate2 = StringVar()

    back_button = Button(track_transaction, text='←', font=('Monaco', 15, 'bold'),
                         bg='#16a9db', fg='#0b046b', activebackground='#16a9db', command=back).pack(anchor=NW)

    # LabelFrame is created
    labelframe = LabelFrame(track_transaction, text='Date Entry', font=(
        'Monaco', 15, 'bold'), bg='#385569', fg='#3ec7f6')
    labelframe.pack(expand='yes', fill='both')
# Buttons are defined and created
    starting_date = Label(labelframe, text='Starting Date:', font=(
        'Monaco', 15, 'bold'), bg='#385569', fg='#3ec7f6')
    starting_date.place(x=430, y=10)
    date_entry = DateEntry(labelframe, textvariable=tempdate1)
    date_entry.place(x=630, y=10)

    end_date = Label(labelframe, text='Ending Date  :', font=(
        'Monaco', 15, 'bold'), bg='#385569', fg='#3ec7f6')
    end_date.place(x=430, y=40)
    end_date_entry = DateEntry(labelframe, textvariable=tempdate2)
    end_date_entry.place(x=630, y=40)

    show_button = Button(labelframe, text='Show', font=('Monaco', 20, 'bold'), bg='#16a9db',
                         fg='#0b046b', activebackground='#16a9db', command=SHOW).place(x=570, y=90)

    labelframe = LabelFrame(track_transaction, text='Details', font=(
        'Monaco', 15, 'bold'), bg='#385569', fg='#3ec7f6')
    labelframe.pack(expand='yes', fill='both')

    earn_money = Label(labelframe, text='Total Money Earn     :', font=(
        'Monaco', 15, 'bold'), bg='#385569', fg='#3ec7f6')
    earn_money.place(x=430, y=10)
    starting_date_entry = Entry(
        labelframe, width=20, textvariable=moneyearn, font=('Monaco', 15, 'bold'))
    starting_date_entry.place(x=730, y=10)

    spend_money = Label(labelframe, text='Total Money Spend    :', font=(
        'Monaco', 15, 'bold'), bg='#385569', fg='#3ec7f6')
    spend_money.place(x=430, y=40)
    spend_money_entry = Entry(
        labelframe, width=20, textvariable=moneyspend, font=('Monaco', 15, 'bold'))
    spend_money_entry.place(x=730, y=40)

    money_available = Label(labelframe, text='Total Money Available:', font=(
        'Monaco', 15, 'bold'), bg='#385569', fg='#3ec7f6')
    money_available.place(x=430, y=70)
    money_available_entry = Entry(
        labelframe, width=20, textvariable=moneyavailabel, font=('Monaco', 15, 'bold'))
    money_available_entry.place(x=730, y=70)

    clear_button = Button(labelframe, text='Clear', font=('Monaco', 20, 'bold'), bg='#16a9db',
                          fg='#0b046b', activebackground='#16a9db', command=CLEAR).place(x=570, y=100)

    labelframe = LabelFrame(track_transaction, text='Graphical Representation', font=(
        'Monaco', 15, 'bold'), bg='#385569', fg='#3ec7f6')
    labelframe.pack(expand='yes', fill='both')

    plot = Label(labelframe, text='Plot:', font=(
        'Monaco', 15, 'bold'), bg='#385569', fg='#3ec7f6')
    plot.place(x=430, y=10)

    plotlist = ['Bar Chart',]
    clickedoption = StringVar(labelframe)
    security_question_entry = ttk.OptionMenu(
        labelframe, clickedoption, *plotlist).place(x=500, y=10)

    view_button = Button(labelframe, text='View', font=('Monaco', 20, 'bold'), bg='#16a9db',
                         fg='#0b046b', activebackground='#16a9db', command=VIEW).place(x=575, y=70)
    track_transaction.mainloop()
