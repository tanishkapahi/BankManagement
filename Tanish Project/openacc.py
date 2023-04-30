from tkinter import *
import pymysql
from PIL import ImageTk, Image
from tkinter import messagebox
import datetime

class open:
    def __init__(self):
        self.root=Tk()
        self.root.geometry("740x640")
        self.root.resizable(False, False)
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
        self.l1=Label(self.root, text='Account Number', background='maroon', foreground='yellow',
        font=('Arial', 10, 'bold'))
        self.l1.place(relx=0.38, rely=0.16,width=100, height=20)
        self.e1 = Entry(self.root,background='lightgrey')
        self.e1.place(relx=0.53, rely=0.16, height=20, width=180)
        
        self.l2=Label(self.root, text='Customer Name', background='maroon', foreground='yellow',
        font=('Arial', 10, 'bold'))
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
        today=datetime.datetime.now()
        t= datetime.datetime.date(today)
        self.e9 = Entry(self.root,background='lightgrey')
        self.e9.insert(1, t)
        self.e9.config(state='disabled')
        self.e9.place(relx=0.53, rely=0.72, height=20, width=180)
        
        self.l10=Label(self.root, text='Balance', background='maroon', foreground='yellow',
        font=('Arial', 10, 'bold'))
        self.l10.place(relx=0.38, rely=0.79,width=100, height=20)
        self.e10= Entry(self.root,background='lightgrey')
        self.e10.place(relx=0.53, rely=0.79, height=20, width=180)
        
        #button login
        self.b1=Button(self.root, text='Create Account',command=self.open)
        self.b1.place(relx=0.46, rely=0.86, height =40, width=120)
        
        self.root.mainloop()
        
    def open(self):
        self.accno = self.e1.get()
        self.cname = self.e2.get()
        self.add = self.e3.get(1.0,END)
        self.cgen = self.e4.get()
        self.cemail = self.e5.get()
        self.cmob = self.e6.get()
        self.cfname = self.e7.get()
        self.cmname= self.e8.get()
        self.odate= self.e9.get()
        self.balance = self.e10.get()
        
        conn= pymysql.connect(host='localhost', user='root', password='root', db='dbbank')
        cursor= conn.cursor()
        
        messagebox.showinfo('Banking System', 'Account Created Successfully')
        
        cursor.execute('insert into tbaccount values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(self.accno, self.cname, self.add,self.cgen,
        self.cemail, self.cmob, self.cfname, self.cmname, self.odate, self.balance))
        
        conn.commit()
        
