from tkinter import *
top = Tk()
top.geometry('500x500+100+200') # width =500 , height=500 ,100px from right , 200px from bottom 
# top.state('zoomed')
top.title("My first GUI applicatiion")
fname = input("Enter the name of the file")
l1 = Label (text="Enter your name",font=('tahoma',12,'bold'))
t1 = Entry(font=('tahoma',12,'bold'))
l2 = Label(text="Enter your email id ",font=('Sen Serif',12,'bold'))
t2 = Entry(font=('tahoma',12,'bold'))
b1 = Button(text = 'Submit',font=('tahoma',12,'bold'))
l1.pack()
t1.pack()
l2.pack()
t2.pack()
b1.pack()
top.mainloop()
   