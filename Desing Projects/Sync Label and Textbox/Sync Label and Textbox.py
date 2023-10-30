from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

app=tb.Window(themename='superhero')
app.title('TTK BOOTSTRAP')       
app.iconbitmap('C:/Users/Musab/Desktop/kmd/Phyton/empty.ico')
app.geometry('600x600')
app.resizable(False,False)

var1=tb.StringVar()

def hi():
    print('hi')
    print(var1.get())


l1=tb.Label(app,textvariable=var1,bootstyle='primary',anchor='center').pack(expand=True,fill='both',pady=10)

b1=tb.Button(app,text='button1',bootstyle='primary outline',command=hi).pack(expand=True,fill='both',pady=10)

e1=tb.Entry(app,bootstyle='danger',textvariable=var1).pack(expand=True,fill='both',pady=10)

app.mainloop()
