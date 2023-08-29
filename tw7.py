import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title("Simple calculator")
root.geometry("600x450")

Frame=ttk.Frame(root,padding=" 50 50 50 50")
Frame.pack()

ttk.Label(Frame,text="ENTER 1st NUMBER").grid(columnspan=4,column=0,row=0)
no1=tk.StringVar()
ttk.Entry(Frame,width=60,textvariable=no1).grid(columnspan=4,column=0,row=1)

ttk.Label(Frame,text="Enter 2nd Number").grid(columnspan=4,column=0,row=2)
no2=tk.StringVar()
ttk.Entry(Frame,width=60,textvariable=no2).grid(columnspan=4,column=0,row=3)

def add():
    n1=float(no1.get())
    n2=float(no2.get())
    res.set(n1+n2)

def sub():
    n1=float(no1.get())
    n2=float(no2.get())
    res.set(n1-n2)

def mul():
    n1=float(no1.get())
    n2=float(no2.get())
    res.set(n1*n2)
    
def dvd():
    n1=float(no1.get())
    n2=float(no2.get())
    if n2==0:
        res.set("Cant divide")
    else:
        res.set(n1/n2)
    
ttk.Button(Frame,text="ADD",command=add).grid(column=0,row=4)
ttk.Button(Frame,text="SUB",command=sub).grid(column=1,row=4)
ttk.Button(Frame,text="MUL",command=mul).grid(column=2,row=4)
ttk.Button(Frame,text="DVD",command=dvd).grid(column=3,row=4)

ttk.Label(Frame,text="ANSWER").grid(column=0,row=6,columnspan=3)
res=tk.StringVar()
ttk.Entry(Frame,width=10, textvariable=res,state="readonly").grid(column=3,row=6,columnspan=1)


root.mainloop()