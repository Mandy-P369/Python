# It is just the basic program to find the Simple interest 
def fun1():
    principle  = int(t1.get())
    rate = float(t2.get())
    time  = int(t3.get())
    simple_interest = principle*rate*time/100
    l5.config(text=simple_interest)

from tkinter import *
top = Tk()
top.geometry('1000x500+100+100')
l1 = Label(text="Principle : ",font=('San Serif',18,'bold'))
l2 = Label(text="Rate : ",font=('San Serif',18,'bold'))
l3 = Label(text="Time : ",font=('San Serif',18,'bold'))
l4 = Label(text="Simple Interest : ",font=('San Serif',18,'bold'))
l5 = Label(font=('San Serif',18,'bold'))
t1 = Entry(font=('tahoma',15,'bold'))
t2 = Entry(font=('tahoma',15,'bold'))
t3 = Entry(font=('tahoma',15,'bold'))
b1 = Button(text='submit', font=('tahoma',15,'bold'),command=fun1)
l1.pack()
t1.pack()
l2.pack()
t2.pack()
l3.pack()
t3.pack()
l4.pack()
l5.pack()
b1.pack()

top.mainloop()