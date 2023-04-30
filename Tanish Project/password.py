from tkinter import *
#from tkinter.ttk import *
import pymysql
from PIL import ImageTk, Image
from tkinter import messagebox
class Password:
    def __init__(self):
        
        self.root=Tk()
        self.root.geometry("840x500")
        #self.root.resizable(False, False)
        self.root.config(background='lightyellow')
        
        #frame
        self.f1 = Frame(self.root,  height =300, width =300 ,relief = RIDGE, bd=5,background='lightyellow') 
        self.f1.place(relx=0.221, rely=0.350)
        
         #image
        self.i1= ImageTk.PhotoImage(Image.open("login.png"))
        self.l2=Label(self.f1,background='lightyellow')
        self.l2.config(image=self.i1)
        self.l2.pack()
        
        
        #banking label
        self.l1=Label(self.root, text='Banking System', background='maroon', foreground='yellow',
        font=('Arial', 24, 'bold'))
        self.l1.place(relx=0.50, rely=0.20, anchor='center', height=120, width=420)
        
        #username label
        self.l1=Label(self.f1, text='New password', background='maroon', foreground='yellow',
        font=('Arial', 10, 'bold'))
        self.l1.place(relx=0.12, rely=0.36,width=105)
        
        #username textbox
        self.e1 = Entry(self.f1,background='lightgrey')
        self.e1.place(relx=0.40, rely=0.36, height=20)
        
        #password label
        self.l1=Label(self.f1, text='Confirm new password', background='maroon', foreground='yellow',
        font=('Arial', 10, 'bold'))
        self.l1.place(relx=0.02, rely=0.46,width=150)
        
        #password textbox
        self.e2 = Entry(self.f1, background='lightgrey',show="*")
        self.e2.place(relx=0.40, rely=0.46,height=20)
        
        #button verify
        self.b1=Button(self.f1, text='Change Password',height=1, width=20, command= self.password)
        self.b1.place(relx=0.35, rely=0.56)
        

        self.root.mainloop()

    def password(self):
        conn= pymysql.connect(host='localhost', user='root', password='root', db='dbbank')
        cursor= conn.cursor()
        
        if(self.e1.get()== self.e2.get()):
            pwd= self.e2.get()
            cursor.execute('update tbadmin set admpwd= %s where admid=%s',(pwd,un))
            conn.commit()
            rows= cursor.rowcount
            if rows>0:
                messagebox.showinfo('Banking System','Password changed successfully')
                self.root.destroy()
            
        else:
            messagebox.showerror('Banking System', 'Both passwords do not match')
            self.e1.delete(0,END)
            self.e2.delete(0,END)
            
l1 =Password()