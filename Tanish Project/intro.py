from tkinter import *
#from tkinter.ttk import *
import pymysql
from PIL import ImageTk, Image
from tkinter import messagebox
from openacc import open
from delete import delete
from modify import modify
from deposit import deposit

class intro:
    def __init__(self):
        self.root=Tk()
        self.root.geometry("640x480")
        self.root.resizable(True, True)
        self.root.title('Banking System')
        self.root.config(background='lightyellow')
        #py
        #self.f1 = Frame(self.root,  height =300, width =300 ,relief = RIDGE, bd=5,background='lightyellow') 
        #self.f1.place(relx=0.221, rely=0.350)
        
         #image
        self.i1= ImageTk.PhotoImage(Image.open("intro.jpg"))
        self.l2=Label(self.root,background='lightyellow')
        self.l2.config(image=self.i1, height =640, width=480)
        self.l2.pack()
        
        #MENU BAR
        self.root.option_add('*tearOff', False)
        self.mb =Menu(self.root)
        self.root.config(menu=self.mb)
        
        self.f = Menu(self.mb)
        self.mb.add_cascade(menu=self.f, label='Account')
        self.f.add_command(label='Open New Account', command=self.open)
        self.f.add_command(label='Modify Account')
        self.f.add_command(label='Delete Account', command=self.delete)
        self.f.add_command(label='View all Accounts')
        self.f.add_command(label='Search')

        self.e = Menu(self.mb)
        self.mb.add_cascade(menu=self.e, label='Transaction')
        self.e.add_command(label='Withdraw')
        self.e.add_command(label='Deposit')
        self.e.add_command(label='Transfer')
        self.e.add_command(label='Mini Statement')

        self.h = Menu(self.mb)
        self.mb.add_cascade(menu=self.h, label='Admin')
        self.h.add_command(label='Edit Profile')
        self.h.add_command(label='Change Password')
        self.h.add_command(label='Modify Security Settings')
        self.h.add_command(label='Logout')
        
        self.c = Menu(self.mb)
        self.mb.add_cascade(menu=self.c, label='Help')
        self.c.add_command(label='About us')
        
        self.root.mainloop()
    def open(self):
        self.root.destroy()
        o1=open()
    def delete(self):
        self.root.destroy()
        d1= delete()
    def modify(self):
        self.root.destroy()
        m1=modify()
    def deposit(self):
        self.root.destroy()
        d1=deposit()
i1=intro()