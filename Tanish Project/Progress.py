from tkinter import *
from tkinter.ttk import Progressbar
from time import *

class progress:
    def __init__(self):
        self.root= Tk()
        self.root.geometry("840x500")
        self.root.config(background='lightyellow')
        #self.root.resizable(False, False)
        self.root.title("Banking System")
        
        self.l1=Label(self.root, text='Please wait while we are loading...')
        self.l1.config(background="maroon",foreground='yellow', font=('Arial', '30', 'bold'))
        self.l1.place(relx=0.50, rely=0.20, anchor='center', height=180, width=1080)
        
        self.v1=IntVar()
        
        self.l2=Label(self.root, text='Loading...', foreground='maroon', font=('Arial', '12', 'bold'))
        self.l2.place(relx=0.09, rely=0.52)
        
        self.pb=Progressbar(self.root, mode='determinate', maximum=100, length=580 )
        self.pb.config(variable = self.v1)
        self.pb.place(relx=0.09, rely=0.58)
       
            
        self.root.mainloop()
#obj=progress()

