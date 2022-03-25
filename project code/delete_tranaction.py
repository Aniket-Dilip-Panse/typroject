from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry

def back():
    delete_transaction.destroy()
    from main_window import main_program
    main_program()

def credit_delete():
    delete_transaction.destroy()
    from main_window import main_program
    main_program()

def del_transaction():
    global delete_transaction
    delete_transaction=Tk()
    delete_transaction.title('DELETE TRANSACTION')
    delete_transaction.geometry('1250x630+10+10')
    # delete_transaction.resizable(0,0)
    delete_transaction.config(bg='#385569')
    delete_transaction.iconbitmap('moneyicon.ico')

    delete_transaction_label=Label(delete_transaction,text='DELETE TRANSACTION',font=('Monaco',35,'bold'),bg='#385569',fg='#3ec7f6').pack()

    labelframe1 = LabelFrame(delete_transaction, text="Delete Credit",font=('Monaco',15,'bold'),bg='#385569',fg='#3ec7f6')  
    labelframe1.pack(fill="both", expand="yes")  
  
    credit_date = Label(labelframe1, text="Date:",font=('Monaco',15,'bold'),bg='#385569',fg='#3ec7f6')  
    credit_date.pack()  

    date=DateEntry(labelframe1,selectmode='day',width=30).pack(pady=7)

    amount_credited = Label(labelframe1, text="Amount Credited:",font=('Monaco',15,'bold'),bg='#385569',fg='#3ec7f6')  
    amount_credited.pack(pady=7)   

    amount_credited_entry=Entry(labelframe1,width=20,font=('Monaco',15,'bold')).pack(pady=7)

    delete_credit_transaction=Button(labelframe1,text='Delete',font=('Monaco',15,'bold'),bg='#16a9db',fg='#0b046b',activebackground='#16a9db',command=credit_delete).pack(pady=5)

  
    labelframe2 = LabelFrame(delete_transaction, text = "Delete Debit",font=('Monaco',15,'bold'),bg='#385569',fg='#3ec7f6')  
    labelframe2.pack(fill="both", expand = "yes")  
  
    debit_date = Label(labelframe2, text = "Date",font=('Monaco',15,'bold'),bg='#385569',fg='#3ec7f6')  
    debit_date.pack() 

    date=DateEntry(labelframe2,selectmode='day',width=30).pack(pady=7)

    expenditure= Label(labelframe2, text="Expenditure:",font=('Monaco',15,'bold'),bg='#385569',fg='#3ec7f6')  
    expenditure.pack(pady=7)   

    expenditur_list=['EMI','Maintainence','Shopping','Food','Health','Entertainment','Travelling','EMI','Other']
    moneyspendclick=StringVar(labelframe2)
    expenditur_list_entry=ttk.OptionMenu(labelframe2,moneyspendclick,*expenditur_list).pack(pady=7)

    amount_debited= Label(labelframe2, text="Amount Debited:",font=('Monaco',15,'bold'),bg='#385569',fg='#3ec7f6')  
    amount_debited.pack(pady=7)

    amount_credited_entry=Entry(labelframe2,width=20,font=('Monaco',15,'bold')).pack(pady=7)

    delete_credit_transaction=Button(labelframe2,text='Delete',font=('Monaco',15,'bold'),bg='#16a9db',fg='#0b046b',activebackground='#16a9db',command=credit_delete).pack(pady=5) 

    back_button=Button(delete_transaction,text='<-',font=('Monaco',20,'bold'),bg='#16a9db',fg='#0b046b',activebackground='#16a9db',command=back).place(x=0,y=0)