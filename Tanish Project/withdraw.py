from tkinter import *
import pymysql
from PIL import ImageTk, Image
from tkinter import messagebox
import datetime

class withdraw:
    def __init__(self):
        self.root=Tk()
        self.root.geometry("1280x768")
        self.root.resizable(True, False)
        self.root.title('Banking System')
        self.root.config(background='lightyellow')
        
         #image
        img= Image.open("openacc.png")
        self.i2= img.resize((250,250))#, Image.ANTIALIAS)
        self.i1=ImageTk.PhotoImage(self.i2)
        self.l1=Label(self.root,background='lightyellow')
        self.l1.config(image=self.i1)#, height =200, width=250)
        self.l1.grid(row=0, column=0)
        
        #text box and Labels
        self.l1=Label(self.root, text='Enter Account Number', background='maroon', foreground='yellow',
        font=('Arial', 10, 'bold'))
        self.l1.place(relx=0.38, rely=0.06,width=160, height=20)
        self.e1 = Entry(self.root,background='lightgrey')
        self.e1.place(relx=0.65, rely=0.06, height=20, width=180)
        
        #button verify
        self.b1=Button(self.root, text='Verify',command=self.verify)
        self.b1.place(relx=0.50, rely=0.11, height =30, width=100)        
        
        self.root.mainloop()
        
        
    def verify(self):
        conn= pymysql.connect(host='localhost', user='root', password='root', db='dbbank')
        cursor= conn.cursor()

        un= self.e1.get()

        cursor.execute('select * from tbaccount where accno = %s',un)
        conn.commit()
        rows= cursor.rowcount
        if rows>0:
            messagebox.showinfo('Banking System','Account Found')
            
            row= cursor.fetchone()
            self.l2=Label(self.root, text='Customer Name', background='maroon', foreground='yellow',
            font=('Arial', 10, 'bold'))
            self.l2.place(relx=0.38, rely=0.23,width=100, height=20)
            
            self.l2.place(relx=0.38, rely=0.23,width=100, height=20)
            self.e2 = Entry(self.root,background='lightgrey')
            self.e2.place(relx=0.53, rely=0.23, height=20, width=180)
        
            self.l3=Label(self.root, text='Address', background='maroon', foreground='yellow',
            font=('Arial', 10, 'bold'))
            self.l3.place(relx=0.38, rely=0.30,width=100, height=20)
            self.e3 = Text(self.root,background='lightgrey')
            self.e3.place(relx=0.53, rely=0.30, height=45, width=200)
        
            self.l4=Label(self.root, text='Gender', background='maroon', foreground='yellow',
            font=('Arial', 10, 'bold'))
            self.l4.place(relx=0.38, rely=0.37,width=100, height=20)
            self.e4 = Entry(self.root,background='lightgrey')
            self.e4.place(relx=0.53, rely=0.37, height=20, width=180)
        
            self.l5=Label(self.root, text='Email ID', background='maroon', foreground='yellow',
        font=('Arial', 10, 'bold'))
            self.l5.place(relx=0.38, rely=0.44,width=100, height=20)
            self.e5 = Entry(self.root,background='lightgrey')
            self.e5.place(relx=0.53, rely=0.44, height=20, width=180)
        
            self.l6=Label(self.root, text='Mobile', background='maroon', foreground='yellow',
        font=('Arial', 10, 'bold'))
            self.l6.place(relx=0.38, rely=0.51,width=100, height=20)
            self.e6 = Entry(self.root,background='lightgrey')
            self.e6.place(relx=0.53, rely=0.51, height=20, width=180)
        
            self.l7=Label(self.root, text='Father Name', background='maroon', foreground='yellow',
        font=('Arial', 10, 'bold'))
            self.l7.place(relx=0.38, rely=0.58,width=100, height=20)
            self.e7 = Entry(self.root,background='lightgrey')
            self.e7.place(relx=0.53, rely=0.58, height=20, width=180)
        
            self.l8=Label(self.root, text='Mother Name', background='maroon', foreground='yellow',
        font=('Arial', 10, 'bold'))
            self.l8.place(relx=0.38, rely=0.65,width=100, height=20)
            self.e8 = Entry(self.root,background='lightgrey')
            self.e8.place(relx=0.53, rely=0.65, height=20, width=180)
        
            self.l9=Label(self.root, text='Opening Date', background='maroon', foreground='yellow',
        font=('Arial', 10, 'bold'))
            self.l9.place(relx=0.38, rely=0.72,width=100, height=20)
            self.e9 = Entry(self.root,background='lightgrey')
            
            self.e9.place(relx=0.53, rely=0.72, height=20, width=180)
        
            self.l10=Label(self.root, text='Balance', background='maroon', foreground='yellow',
        font=('Arial', 10, 'bold'))
            self.l10.place(relx=0.38, rely=0.79,width=100, height=20)
            self.e10= Entry(self.root,background='lightgrey')
            self.e10.place(relx=0.53, rely=0.79, height=20, width=180)
           
            self.e2.insert(6, row[1])
            self.e3.insert('1.0', row[2])
            self.e4.insert(0, row[3])
            self.e5.insert(0, row[4])
            self.e6.insert(0, row[5])
            self.e7.insert(0, row[6])
            self.e8.insert(0, row[7])
            self.e9.insert(0, row[8])
            self.e10.insert(0, row[9])
            self.e2.config(state='disabled')
            self.e3.config(state='disabled')
            self.e4.config(state='disabled')
            self.e5.config(state='disabled')
            self.e6.config(state='disabled')
            self.e7.config(state='disabled')
            self.e8.config(state='disabled')
            self.e9.config(state='disabled')
            self.e10.config(state='disabled')
            
            
            self.l11=Label(self.root, text='Withdraw Amount', background='maroon', foreground='yellow',
        font=('Arial', 10, 'bold'))
            self.l11.place(relx=0.38, rely=0.86,width=120, height=20)
            self.e11= Entry(self.root,background='lightgrey')
            self.e11.place(relx=0.53, rely=0.86, height=20, width=180)
            
            self.b2=Button(self.root, text='Withdraw',command=self.withdraw)
            self.b2.place(relx=0.73, rely=0.86, height =30, width=100)     
            
        else:
            messagebox.showerror('Banking System', 'No such Account')
            self.e1.delete(0,END)
    def withdraw(self):
        conn= pymysql.connect(host='localhost', user='root', password='root', db='dbbank')
        cursor= conn.cursor()
        amt= int(self.e11.get())
        bal= int(self.e10.get())
        if(bal>=amt):
            
            newbalance=bal-amt
            print(newbalance)

            cursor.execute('update tbaccount set balance =%s',newbalance)
            messagebox.showinfo('Banking System', 'Amount Withdrawn Successfully')
            conn.commit()
        else:
            messagebox.showerror('Banking System', 'Insufficient Balance')
            self.e11.delete(0,END)
        
        
d1=withdraw()