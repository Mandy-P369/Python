global language
def showLanguage():
    global language
    print('The language is :')
    lang = lan.get()
    if lang==1:
        language = 'Python'
    elif lang==2:
        language = 'Java'
    elif lang==3:
        language ='C'
    else :
        language = 'C++'
    print('The language is: ',language)
    l4.config(text=language)

global finalpay
def Salary():
    global finalpay
    sal = cmb.get()
    if sal==40000:
        finalpay = int(sal) + int(sal) * 0.1
    elif sal==60000:
        finalpay = int(sal) + int(sal) * 0.1
    elif sal==80000:
        finalpay = int(sal) + int(sal) * 0.1
    else:
        finalpay = int(sal) + int(sal) * 0.1
    l6.config(text=finalpay)

from tkinter import *
from tkinter import ttk
top = Tk()
top.state('zoomed')
fnt = ('arial',15,'bold')
l1= Label(text='username',font=fnt)
l2 = Label(text='password',font=fnt)
t1= Entry(width=40,font=fnt)
t2 = Entry(width=40,font=fnt,show='*')

# Button
b1 = Button(text='Login',font=fnt)
b2 = Button(text='Logout',font=fnt)
b3 =Button(text='Exit',font=fnt)

# Scale
sc=Scale(orient=HORIZONTAL,font=fnt,from_=1,to=7)
sc1=Scale(orient=VERTICAL,font=fnt,from_=1 ,to=100)

# Spin box
spin = Spinbox(from_=1,to=100,font=fnt)
spin2 = Spinbox(from_=10 ,to=200,font=fnt)

# RadioButton
l3 = Label(text='Select Language ',font=fnt)
lan = IntVar()
rb1 = Radiobutton(text='Python',font=fnt,value=1,variable=lan)
rb2 = Radiobutton(text='Java',font=fnt,value=2,variable=lan)
rb3 = Radiobutton(text='C',font=fnt,value=3,variable=lan)
rb4 = Radiobutton(text='C++',font=fnt,value=4,variable=lan)
b4 = Button(text='show language',font=fnt,command=showLanguage)
l4 = Label(font=fnt)

# Combobox()
l5 = Label(text='Salary',font=fnt)
values = [40000,60000,80000,100000]
cmb = ttk.Combobox(values=values,font=fnt)
l6 = Label(font=fnt)
b5 = Button(text='Salary',font=fnt,command=Salary)

# Packing all the controls
l1.grid(row=0,column=0)
t1.grid(row=0,column=1)
l2.grid(row=2,column=0)
t2.grid(row=2,column=1)
b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
sc.grid(row=4,column=0)
sc1.grid(row=4,column=1)
spin.grid(row=5,column=0)
spin2.grid(row=5,column=1)

# ---------------------------

l3.grid(row=6,column=0)
rb1.grid(row=6,column=1)
rb2.grid(row=6,column=2)
rb3.grid(row=6,column=3)
rb4.grid(row=7,column=0)
b4.grid(row=8,column=1)
l4.grid(row=7,column=1)
cmb.grid(row=8,column=2)
l6.grid(row=10,column=2)
b5.grid(row=9,column=2)

top.mainloop()