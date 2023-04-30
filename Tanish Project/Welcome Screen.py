from tkinter import *
from tkinter import ttk
from Progress import progress
class welcome:
    def __init__(self):
        self.root= Tk()
        self.root.geometry("840x500")
        #self.root.resizable(False, False)
        self.root.config(background='lightyellow')
        self.root.title('Banking System')
        self.l1=Label(self.root, text='Banking System')
        self.l1.config(background="maroon",foreground='yellow', font=('Arial', '34', 'bold'))
        self.l1.place(relx=0.50, rely=0.20, anchor='center', height=180, width=1080)
        
        self.b1= Button(self.root, text='Click here to continue', command= self.progress)
        self.b1.place(relx=0.50, rely=0.60, anchor='center', height=40, width=216)
        
        self.root.mainloop()
    def progress (self):
        self.root.destroy()
        obj=progress()
        
obj= welcome()