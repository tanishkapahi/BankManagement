from tkinter import *
import pymysql
from PIL import ImageTk, Image
from tkinter import messagebox
import datetime

class transfer():
    def __init__(self):
        self.root=Tk()
        self.root.geometry("1280x768")
        self.root.resizable(True, False)
        self.root.title('Banking System')
        self.root.config(background='lightyellow')
        
        img= Image.open("bank.png")
        self.i2= img.resize((150,150))#, Image.ANTIALIAS) #reduce image size
        self.i1=ImageTk.PhotoImage(self.i2)
        self.l1=Label(self.root,background='lightyellow')
        self.l1.config(image=self.i1)#, height =200, width=250)
        self.l1.place(relx=0.05, rely=0.06)
        
        #source account number
        self.l1=Label(self.root, text='Enter Source Account Number', background='maroon', foreground='yellow',
        font=('Arial', 10, 'bold'))
        self.l1.place(relx=0.32, rely=0.06,width=200, height=20)
        self.e1 = Entry(self.root,background='lightgrey')
        self.e1.place(relx=0.60, rely=0.06, height=20, width=180)
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
            
            self.l3=Label(self.root, text='Current Balance', background='maroon', foreground='yellow',
            font=('Arial', 10, 'bold'))
            self.l3.place(relx=0.32, rely=0.26,width=200, height=20)
            self.e3 = Entry(self.root,background='lightgrey')
            self.e3.place(relx=0.60, rely=0.26, height=20, width=180)
            bal= cursor.execute('select balance from tbaccount where accno=%s',un)
            for bal in cursor:
                print(bal)
            self.e3.insert(0,bal)
            self.e3.config(state='disabled')
            
            
            self.f1 = Frame(self.root,  height =300, width =600 ,relief = RIDGE, bd=5,background='lightyellow') 
            self.f1.place(relx=0.311, rely=0.350)
                #destination account number
            self.l2=Label(self.root, text='Enter Destination Account Number', background='maroon', foreground='yellow',
            font=('Arial', 10, 'bold'))
            self.l2.place(relx=0.32, rely=0.41,width=230, height=20)
            self.e2 = Entry(self.root,background='lightgrey')
            self.e2.place(relx=0.60, rely=0.41, height=20, width=180)
        #button verify
            self.b2=Button(self.root, text='Verify',command=self.verify1)
            self.b2.place(relx=0.50, rely=0.46, height =30, width=100)
        
        else:
            messagebox.showerror('Banking System', 'No such Account')
            self.e1.delete(0,END)
            
    def verify1(self):
        conn= pymysql.connect(host='localhost', user='root', password='root', db='dbbank')
        cursor= conn.cursor()

        un1= self.e2.get()

        cursor.execute('select * from tbaccount where accno = %s',un1)
        conn.commit()
        rows= cursor.rowcount
        if rows>0:
            messagebox.showinfo('Banking System','Account Found')
            
            
        #transfer amount
            self.l4=Label(self.root, text='Enter transfer amount', background='maroon', foreground='yellow',
            font=('Arial', 10, 'bold'))
            self.l4.place(relx=0.32, rely=0.61,width=230, height=20)
            self.e4 = Entry(self.root,background='lightgrey')
            self.e4.place(relx=0.60, rely=0.61, height=20, width=180)
        #button verify
            self.b3=Button(self.root, text='Transfer')
            self.b3.place(relx=0.50, rely=0.66, height =30, width=100)
        else:
            messagebox.showerror('Banking System', 'No such Account')
            self.e1.delete(0,END)
t1=transfer()