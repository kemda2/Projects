####################################################################################################
################################################## Tkinter TTKBootstrap 2 Label and Button
####################################################################################################

# from tkinter import *
# from ttkbootstrap.constants import *
# import ttkbootstrap as tb


# root=tb.Window(themename="superhero")
# root.title("")
# root.geometry('700x700')

# counter=0

# def changer ():
#     global counter
#     counter += 1
    
#     if counter % 2 == 0:
#         label.config(text="Hello World")
#     else:
#         label.config(text="Goodbye World!")   
    

# label=tb.Label(master=root, 
#         text='Hello World!',
#         font=('Helvetica',28),
#         bootstyle="warning, inverse")
# label.pack(pady=50)
# # tb.Label(master=root, 
# #         text='World!',
# #         font=('Helvetica',28),
# #         bootstyle="warning").pack(pady=50)

# # tb.Button(master=root,
# #           text='Click Me!',
# #           bootstyle="primary").pack(pady=20)

# # tb.Button(master=root,
# #           text='Click Me!',
# #           bootstyle="success, outline").pack(pady=20)

# button=tb.Button(master=root,
#           text='Click Me!',
#           bootstyle="success, link",
#           command=changer)
# button.pack(pady=20)

# root.mainloop()


####################################################################################################
################################################## Tkinter TTKBootstrap 3 Modern Checkbuttons, Toolbuttons, and Togglebuttons
####################################################################################################

# from tkinter import *
# from ttkbootstrap.constants import *
# import ttkbootstrap as tb


# root=tb.Window(themename="superhero")
# root.title("")
# root.iconbitmap('empty.ico')
# root.geometry('700x700')

# def checker():
#     if var1.get() == 1:
#         label.config(text="Checked!")
#     else:
#         label.config(text="Unchecked!")

# label=Label(text='Click the checkbutton below!',
#             font=('Helvetica',28))
# label.pack(pady=(40,10))

# var1=IntVar()
# check=tb.Checkbutton(bootstyle="primary",
#                        text='check me out',
#                        variable=var1,
#                        onvalue=1,
#                        offvalue=0,
#                        command=checker)

# check.pack(pady=10)

# var2=IntVar()
# check2=tb.Checkbutton(bootstyle="danger,toolbutton",
#                       text="ToolButton!!",
#                       variable=var2,
#                       onvalue=1,
#                       offvalue=0,
#                       command=checker)
# check2.pack(pady=10)

# var3=IntVar()
# check3=tb.Checkbutton(bootstyle="danger,toolbutton,outline",
#                       text="Outlined ToolButton!!",
#                       variable=var3,
#                       onvalue=1,
#                       offvalue=0,
#                       command=checker)
# check3.pack(pady=10)

# var4=IntVar()
# check4=tb.Checkbutton(bootstyle="success,round-toggle",
#                       text="round-toggle!!",
#                       variable=var4,
#                       onvalue=1,
#                       offvalue=0,
#                       command=checker)
# check4.pack(pady=10)

# var5=IntVar()
# check5=tb.Checkbutton(bootstyle="success,square-toggle",
#                       text="square-toggle!!",
#                       variable=var5,
#                       onvalue=1,
#                       offvalue=0,
#                       command=checker)
# check5.pack(pady=10)

# root.mainloop()

####################################################################################################
################################################## Tkinter TTKBootstrap 4 How To Resize Buttons in TTKBootstrap
####################################################################################################

# from tkinter import *
# from ttkbootstrap.constants import *
# import ttkbootstrap as tb


# root=tb.Window(themename="superhero")
# root.title("")
# root.iconbitmap('empty.ico')
# root.geometry('700x700')

# my_style=tb.Style()
# my_style.configure('success.Outline.TButton',font=('Helvetica',18))

# button=tb.Button(text="Hello World!",
#                  bootstyle='success',
#                  style="success.Outline.TButton")
# button.pack(pady=40)

# root.mainloop()

####################################################################################################
################################################## Tkinter TTKBootstrap 5 ComboBoxes and Bindings
####################################################################################################

# from tkinter import *
# from ttkbootstrap.constants import *
# import ttkbootstrap as tb


# root=tb.Window(themename="superhero")
# root.title("")
# root.iconbitmap('empty.ico')
# root.geometry('700x700')

# def clicker():
#     label.config(text=f"{combo.get()} was saved!")

# def click_bind(e):
#     label.config(text=f"You selected {combo.get()}!")
    

# label=tb.Label(root,text="Hello World!",font=("Helvetica",18))
# label.pack(pady=30)

# days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

# combo=tb.Combobox(root,bootstyle="success",values=days)
# combo.pack(pady=20)
# combo.current(0)

# button=tb.Button(root,text="Click Me!",command=clicker,bootstyle="danger")
# button.pack(pady=20)

# combo.bind("<<ComboboxSelected>>",click_bind)

# root.mainloop()


####################################################################################################
################################################## Tkinter TTKBootstrap 6 Entry Widgets With TTKBootstrap
####################################################################################################

# from tkinter import *
# from ttkbootstrap.constants import *
# import ttkbootstrap as tb


# root=tb.Window(themename="superhero")
# root.title("")
# root.iconbitmap('empty.ico')
# root.geometry('700x700')

# def speak():
#     label.config(text=f'You Typed: {entry.get()}')

# entry=tb.Entry(root,
#                bootstyle="success",
#                font=("Helvetica",18),
#                foreground="green",
#                width=15,
#                show="*")
# entry.pack(pady=50)

# button=tb.Button(root,
#                  text="Click Me!",
#                  command=speak,
#                  bootstyle="danger outline")
# button.pack(pady=20)

# label=tb.Label(root,
#                text="",
#                font=("Helvetica",18))
# label.pack(pady=20)

# root.mainloop()


####################################################################################################
################################################## Tkinter TTKBootstrap 7 Floodgauge Progress Bar 
####################################################################################################

# from tkinter import *
# from ttkbootstrap.constants import *
# import ttkbootstrap as tb

# root=tb.Window(themename="superhero")
# root.title("")
# root.iconbitmap('empty.ico')
# root.geometry('700x700')

# def starter():
#     gauge.start()

# def stopper():
#     gauge.stop()

# def incrementer():
#     gauge.step(10)
#     label.config(text=f"Position: {gauge.variable.get()}")

# gauge=tb.Floodgauge(root,
#                     bootstyle="success",
#                     font=("Helvetica",18),
#                     mask="Pos:  {}%",
#                     maximum=80,
#                     orient="horizontal",
#                     value=0,
#                     mode="determinate") # indetermine sonsuza kadar devam eder
# gauge.pack(pady=50,fill="x",padx=20)

# start_button=tb.Button(root,
#                  text="Start",
#                  bootstyle="danger outline",
#                  command=starter)
# start_button.pack(pady=20)

# stop_button=tb.Button(root,
#                  text="stop",
#                  bootstyle="danger outline",
#                  command=stopper)
# stop_button.pack(pady=20)

# inc_button=tb.Button(root,
#                  text="Increment",
#                  bootstyle="danger outline",
#                  command=incrementer)
# inc_button.pack(pady=20)

# label=tb.Label(root,text=f"Position: ")
# label.pack(pady=20)

# root.mainloop()

####################################################################################################
################################################## Tkinter TTKBootstrap 8 DateEntry Calendar Widget
####################################################################################################

# from tkinter import *
# import ttkbootstrap as tb
# from ttkbootstrap.constants import *
# from datetime import date
# from ttkbootstrap.dialogs import Querybox

# root=tb.Window(themename="superhero")

# root.title("")
# root.iconbitmap('empty.ico')
# root.geometry('500x500')

# def getdate():
    
#     label1.config(text=f'You Picked: {date1.entry.get()}')

# def thing():
#     cal = Querybox
#     label1.config(text=f"You Picked: {cal.get_date()}")

# date1=tb.DateEntry(root,bootstyle="danger",firstweekday=0) # ,startdate=date(2023,2,14) başlangıcı belirleme 
# date1.pack(pady=50)
# button1=tb.Button(root,text='Get Date',bootstyle='danger outline',command=getdate) 
# button1.pack(pady=20)
# button2=tb.Button(root,text='Get Calendar',bootstyle='success outline',command=thing) 
# button2.pack(pady=20)
# label1=tb.Label(root,text='')
# label1.pack(pady=20)

# root.mainloop()

####################################################################################################
################################################## Tkinter TTKBootstrap 9 Frames and Labels with TTKBootstrap
####################################################################################################

# from tkinter import *
# import ttkbootstrap as tb
# from ttkbootstrap.constants import *


# root=tb.Window(themename="superhero")

# root.title("")
# root.iconbitmap('empty.ico')
# root.geometry('500x500')

# frame1=tb.Frame(root,bootstyle="light")
# frame1.pack(pady=(40,20))

# entry1=tb.Entry(frame1,font=('Helvetica',18))
# entry1.pack(pady=20,padx=20)

# def thing():
#     pass

# button1=tb.Button(frame1,text='CLICK ME!',bootstyle='dark',command=thing) 
# button1.pack(pady=20,padx=20)

# label1=tb.Label(root,text='Hello There!',font=('Helvetica',18),bootstyle="inverse light")
# label1.pack(pady=20)

# root.mainloop()


####################################################################################################
################################################## Tkinter TTKBootstrap 10 Menu Buttons with TTKBootstrap
####################################################################################################

# from tkinter import *
# import ttkbootstrap as tb
# from ttkbootstrap.constants import *


# root=tb.Window(themename="superhero")

# root.title("")
# root.iconbitmap('empty.ico')
# root.geometry('500x500')

# def stuff(x):
#     menu.config(bootstyle=x)
#     label.config(text=f'You selected: {x}')


# menu=tb.Menubutton(root,bootstyle="warning",text="Things!")
# menu.pack(pady=50)

# inside_menu=tb.Menu(menu)

# item_var=StringVar()

# for x in ['primary','secondary','danger','info','outline primary','outline secondary','outline danger','outline info']:
#     inside_menu.add_radiobutton(label=x,variable=item_var,command=lambda x=x: stuff(x))

# menu['menu'] = inside_menu

# label=tb.Label(root,text='')
# label.pack(pady=40)    

# root.mainloop()


####################################################################################################
################################################## Tkinter TTKBootstrap 11 Meters with TTKBootstrap
####################################################################################################

# from tkinter import *
# import ttkbootstrap as tb
# from ttkbootstrap.constants import *


# root=tb.Window(themename="superhero")

# root.title("")
# root.iconbitmap('empty.ico')
# root.geometry('500x600')

# meter=tb.Meter(root,
#                bootstyle='danger', 
#                subtext='Tkinter Learned',
#                interactive=True,
#                textright='%',
#                metertype='full',
#                stripethickness=10,
#                metersize=200,
#                padding=50,
#                amountused=0,
#                amounttotal=100
#                ) # ,textleft='$'  ,metertype='full' can be semi ,stripethickness=10 can be 50 ,metersize=400
# meter.pack(pady=50)

# global counter
# counter=0

# def upper():
#     global counter
    
#     if counter < 100:
#         counter+=5
#         meter.configure(amountused=counter)
#         button.configure(text=f'Click Me For {counter+5}')
#         button2.configure(text=f'Click Me For {counter-5}',state=NORMAL)
    
    
#     if counter == 100:
#         button.configure(text=f'Done',state=DISABLED)
    
#     if counter == 5:
#         button2.configure(text=f'Click Me For {counter-5}',state=NORMAL)
        

# def lower():
#     global counter
    
#     if counter > 0:
#         counter-=5
#         meter.configure(amountused=counter)
#         button.configure(text=f'Click Me For {counter+5}')
#         button2.configure(text=f'Click Me For {counter-5}')
    
#     if counter == 95:
#         button.configure(text=f'Click Me For {counter+5}',state=NORMAL)
    
#     if counter == 0:
#         button2.configure(text=f'Done',state=DISABLED)
    

# button = tb.Button(root,text=f'Click Me For {counter+5}',command=upper)
# button.pack(pady=20)

# button2 = tb.Button(root,text=f'Done',state=DISABLED,command=lower)
# button2.pack(pady=20)

# root.mainloop()

####################################################################################################
################################################## Tkinter TTKBootstrap 12 Notebook Tabs with TTKBootstrap
####################################################################################################

# from tkinter import *
# import ttkbootstrap as tb
# from ttkbootstrap.constants import *


# root=tb.Window(themename="superhero")

# root.title("")
# root.iconbitmap('empty.ico')
# root.geometry('500x600')

# nbook = tb.Notebook(root, bootstyle='dark')
# nbook.pack(pady=20)

# tab1 = tb.Frame(nbook)
# tab2 = tb.Frame(nbook)

# label = Label(tab1,text='My Awesome Label!',font=('Helvetica',18))
# label.pack(pady=20)

# text = Text(tab1,width=70,height=10)
# text.pack(pady=10,padx=10)

# button = tb.Button(tab1,text='Click Me!',bootstyle='danger outline')
# button.pack(pady=20)

# label2 = Label(tab2,text='This is tab2!',font=('Helvetica',18))
# label2.pack(pady=20)

# nbook.add(tab1,text='Tab One')
# nbook.add(tab2,text='Tab Two')

# root.mainloop()


####################################################################################################
################################################## Tkinter TTKBootstrap 13 Progress Bars with TTKBootstrap
####################################################################################################

# from tkinter import *
# import ttkbootstrap as tb
# from ttkbootstrap.constants import *
# import time


# root=tb.Window(themename="superhero")

# root.title("")
# root.iconbitmap('empty.ico')
# root.geometry('500x600')

# prgress=tb.Progressbar(root,bootstyle='danger striped',maximum=100,mode='determinate',length=200,value=0)
# prgress.pack(pady=40)

# frame=tb.Frame(root)
# frame.pack(pady=20)

# def increment():
#     if prgress['value']<100:
#         prgress['value']+=20
#     if prgress['value']==100:
#         button.config(state=DISABLED)
#     label.config(text=prgress['value'])

# def start():
#     prgress.start(10)
#     button.config(state=NORMAL)

# def stop():
#     prgress.stop()
#     button.config(state=NORMAL)

# def auto():
#     for x in range(5):
#         prgress['value']+=20
#         label.config(text=prgress['value'])
#         root.update_idletasks()
#         time.sleep(1)
#     prgress['value']=0   
#     label.config(text=prgress['value'])



# button=tb.Button(frame,text="Increment 20", bootstyle='info',command=increment)
# button.grid(column=0,row=0,padx=10)

# button1=tb.Button(frame,text="Start", bootstyle='info',command=start)
# button1.grid(column=1,row=0,padx=10)

# button2=tb.Button(frame,text="Stop", bootstyle='info',command=stop)
# button2.grid(column=2,row=0,padx=10)

# button3=tb.Button(frame,text="Auto", bootstyle='info',command=auto)
# button3.grid(column=3,row=0,padx=10)

# label=tb.Label(root,text="0",font=("Helvetica",18))
# label.pack(pady=20)

# root.mainloop()

####################################################################################################
################################################## Tkinter TTKBootstrap 14 Radio Buttons with TTKBootstrap
####################################################################################################

# from tkinter import *
# import ttkbootstrap as tb
# from ttkbootstrap.constants import *
# import time


# root=tb.Window(themename="superhero")

# root.title("")
# root.iconbitmap('empty.ico')
# root.geometry('500x600')

# def clicker():
#     label.config(text=f'You Selected: {topping_var.get()}')

# # Create Radio Button List 
# toppings=["Pepperoni", "Cheese", "Veggie"]
# topping_var=StringVar()

# for topping in toppings:
#     tb.Radiobutton(root,bootstyle='danger',variable=topping_var, text=topping,value=topping).pack(pady=20) #,command=clicker 


# button=tb.Button(root,text='Click Me!',command=clicker)
# button.pack(pady=20)

# label=tb.Label(root,text='You Selected: ')
# label.pack(pady=20)

# rb1=tb.Radiobutton(root,bootstyle='info toolbutton',variable=topping_var,text='Radio Button 1',value='Radio Button 1',command=clicker)
# rb1.pack(pady=20)

# rb2=tb.Radiobutton(root,bootstyle='info toolbutton outline',variable=topping_var,text='Radio Button 2',value='Radio Button 2',command=clicker)
# rb2.pack(pady=20)


# root.mainloop()


####################################################################################################
################################################## Tkinter TTKBootstrap 15 Slider / Scales with TTKBootstrap
####################################################################################################

# from tkinter import *
# import ttkbootstrap as tb
# from ttkbootstrap.constants import *
# import time


# root=tb.Window(themename="superhero")

# root.title("")
# root.iconbitmap('empty.ico')
# root.geometry('500x500')

# def scaler(e):
#     label.config(text=f'{int(scale.get())}%')

# scale=tb.Scale(root,
#                bootstyle='warning',
#                length=400,
#                orient='horizontal',
#                from_=0,
#                to=100,
#                command=scaler) # ,state='disable' kapalı ,state='normal' açık
# scale.pack(pady=50)

# label=tb.Label(root,text='',font=('Helvetica',18))
# label.pack()

# root.mainloop()


####################################################################################################
################################################## Tkinter TTKBootstrap 16 Scrollbars with TTKBootstrap
####################################################################################################

# from tkinter import *
# import ttkbootstrap as tb
# from ttkbootstrap.constants import *
# import time


# root=tb.Window(themename="superhero")

# root.title("")
# root.iconbitmap('empty.ico')
# root.geometry('500x500')

# frame = tb.Frame(root)
# frame.pack(pady=20)

# scrool=tb.Scrollbar(frame,orient='vertical',bootstyle='danger round') #danger düz
# scrool.pack(side='right',fill='y')

# text=Text(frame,width=30,height=25,yscrollcommand=scrool.set,wrap='none',font=('Helvetica',18))
# text.pack()

# scrool.config(command=text.yview)

# root.mainloop()


####################################################################################################
################################################## Tkinter TTKBootstrap 17 Separators and Sizegrips with TTKBootstrap
####################################################################################################

# from tkinter import *
# import ttkbootstrap as tb
# from ttkbootstrap.constants import *
# import time


# root=tb.Window(themename="superhero")

# root.title("")
# root.iconbitmap('empty.ico')
# root.geometry('500x500')

# label1=tb.Label(root,text='Label 1',bootstyle='light')
# label1.pack(pady=40)

# sep=tb.Separator(root,bootstyle='info',orient='horizontal') #vertical dikey
# sep.pack(fill='x',padx=100)

# label2=tb.Label(root,text='Label 2',bootstyle='light')
# label2.pack(pady=40)


# sizegrip=tb.Sizegrip(root,bootstyle='info')
# sizegrip.pack(expand=True,fill='both',anchor='se')

# root.mainloop()

####################################################################################################
################################################## Tkinter TTKBootstrap 18 Spinboxes with TTKBootstrap
####################################################################################################

# from tkinter import *
# import ttkbootstrap as tb
# from ttkbootstrap.constants import *
# import time


# root=tb.Window(themename="superhero")

# root.title("")
# root.iconbitmap('empty.ico')
# root.geometry('500x500')

# def spinny():
#     label.config(text=spin.get())

# stuff=['John', 'April', 'Bob', 'Mary']

# spin=tb.Spinbox(bootstyle='success',font=('Helvetica',18),from_=0,to=10,values=stuff,state='readonly',command=spinny) # ,command=spinny silersen buttonla label içeriğini değiştirir
# spin.pack(pady=40)

# spin.set('John')

# button=tb.Button(root,text='Click Me!',command=spinny,bootstyle='success')
# button.pack(pady=20)

# label=tb.Label(root,text='',font=('Helvetica',18))
# label.pack(pady=20)

# root.mainloop()


####################################################################################################
################################################## Tkinter TTKBootstrap 19 Treeviews with TTKBootstrap
####################################################################################################

# from tkinter import *
# import ttkbootstrap as tb
# from ttkbootstrap.constants import *
# import time


# root=tb.Window(themename="superhero")

# root.title("")
# root.iconbitmap('empty.ico')
# root.geometry('700x500')

# columns = ("first_name",'last_name','email')

# tree=tb.Treeview(root,bootstyle='success',columns=columns,show='headings')
# tree.pack(pady=20)

# tree.heading('first_name',text='First Name')
# tree.heading('last_name',text='Last Name')
# tree.heading('email',text='Email Adrress')

# contacts=[]

# for n in range(1,20):
#     contacts.append((f'First {n}',f'Last {n}', f'email{n}@address.com'))

# for contact in contacts:
#     tree.insert('',END,values=contact)

# root.mainloop()

####################################################################################################
################################################## Tkinter TTKBootstrap 20 Message Boxes with TTKBootstrap
####################################################################################################

# from tkinter import *
# import ttkbootstrap as tb
# from ttkbootstrap.constants import *
# from ttkbootstrap.dialogs import Messagebox

# root=tb.Window(themename="superhero")
# root.title("")
# # Main App Icon
# root.iconbitmap('empty.ico')
# # MessageBox Icon
# root.iconbitmap(default='empty.ico')
# root.geometry('700x500')

# def clicker ():
#     # create a dialog
#     # yes,no
#     # mb=Messagebox.yesno('Display Message Here','Here is the title')
#     # mb=Messagebox.ok('Display Message Here','Here is the title')
#     # mb=Messagebox.okcancel('Display Message Here','Here is the title')
#     # mb=Messagebox.show_info('Display Message Here','Here is the title')
#     # mb=Messagebox.show_error('Display Message Here','Here is the title')
#     # mb=Messagebox.show_question('Display Message Here','Here is the title')
#     # mb=Messagebox.show_warning('Display Message Here','Here is the title')
#     # mb=Messagebox.yesnocancel('Display Message Here','Here is the title')
#     mb=Messagebox.retrycancel('Display Message Here','Here is the title')
    
#     # display button click
#     # if mb=='No':
#     #     print('no')
#     # else:
#     #     print('yes')
#     label.config(text=f'You Clicked: {mb}')
    

# button=tb.Button(root,text='Click Me!', bootstyle='danger',command=clicker)
# button.pack(pady=40)

# label=tb.Label(root,text='',font=('Helvetica',18))
# label.pack()

# root.mainloop()

####################################################################################################
################################################## Tkinter TTKBootstrap 21 Color Chooser for TTKBootstrap
####################################################################################################

# from tkinter import *
# import ttkbootstrap as tb
# from ttkbootstrap.constants import *
# from ttkbootstrap.dialogs.colorchooser import ColorChooserDialog

# root=tb.Window(themename="superhero")
# root.title("")
# # Main App Icon
# root.iconbitmap('empty.ico')
# # MessageBox Icon
# root.iconbitmap(default='empty.ico')
# root.geometry('700x500')

# def cc():
#     # Create Color Chooser
#     color=ColorChooserDialog()
#     # Show
#     color.show()
    
#     colors=color.result
#     label.config(text=colors.hex)
#     root.configure(background=colors.hex)

# button=tb.Button(root,text='Click Me!',bootstyle='danger',command=cc)
# button.pack(pady=40)

# label=tb.Label(root,text='',font=('Helvetica',18))
# label.pack(pady=10)

# root.mainloop()


####################################################################################################
################################################## Tkinter TTKBootstrap 22 Scrolled Text Widget
####################################################################################################

# from tkinter import *
# import ttkbootstrap as tb
# from ttkbootstrap.scrolled import ScrolledText


# root=tb.Window(themename="superhero")
# root.title("")
# # Main App Icon
# root.iconbitmap('empty.ico')
# root.geometry('700x500')

# text=ScrolledText(root,height=20,width=110,wrap=WORD,bootstyle='danger' ,autohide=True) #
# text.pack(pady=10)


# root.mainloop()


####################################################################################################
################################################## Tkinter TTKBootstrap 23 Scrolled Frame Widget! 
####################################################################################################

# from tkinter import *
# import ttkbootstrap as tb
# from ttkbootstrap.scrolled import ScrolledFrame


# root=tb.Window(themename="superhero")
# root.title("")
# # Main App Icon
# root.iconbitmap('empty.ico')
# root.geometry('700x500')

# frame=ScrolledFrame(root,autohide=False,bootstyle='dark')
# frame.pack(padx=15,pady=15,fill='both',expand=YES)

# for x in range(21):
#     tb.Button(frame,bootstyle='info',text=f'Button {x}').pack(pady=10)

# root.mainloop()


####################################################################################################
################################################## Tkinter TTKBootstrap 24 Toast Messages with TTKBootstrap
####################################################################################################

# from tkinter import *
# import ttkbootstrap as tb
# from ttkbootstrap.toast import ToastNotification


# root=tb.Window(themename="superhero")
# root.title("")
# # Main App Icon
# root.iconbitmap('empty.ico')
# root.geometry('700x500')

# def clicker ():
#     toast.show_toast()

# toast=ToastNotification(title='Toast Title',message='This is the message',position=(-1915,300,'sw')) #,duration=3000

# button=tb.Button(root,text='click me!',command=clicker)
# button.pack(pady=40)

# root.mainloop()


####################################################################################################
################################################## Tkinter TTKBootstrap 25 Icons with TTKBootstrap
####################################################################################################

# from tkinter import *
# import ttkbootstrap as tb
# from ttkbootstrap.icons import Icon


# root=tb.Window(themename="superhero")
# root.title("")
# # Main App Icon
# root.iconbitmap('empty.ico')
# root.geometry('700x500')

# img=PhotoImage(data=Icon.warning) #Icon.icon

# label=tb.Label(image=img)
# label.pack(pady=40)

# root.mainloop()


####################################################################################################
################################################## Tkinter TTKBootstrap 26 Select Fonts With Font Dialog Box 
####################################################################################################

# from tkinter import *
# import ttkbootstrap as tb
# from ttkbootstrap.dialogs import FontDialog


# root=tb.Window(themename="superhero")
# root.title("")
# # Main App Icon
# root.iconbitmap('empty.ico')
# root.geometry('700x500')

# def cc():
#     fd=FontDialog()
#     fd.show()
#     label.config(font=fd.result)

# button=tb.Button(root,text='Open File Dialog!',bootstyle='danger',command=cc)
# button.pack(pady=40)

# label=tb.Label(root,text='Hello World')
# label.pack(pady=10)

# root.mainloop()