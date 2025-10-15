from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("700x700+100+100")
root.resizable(width=0, height=0)
# --------------------------------

# third window
global t
def thirdwindow():
    global t
    t = Toplevel(top)
    t.geometry("300x300+100+100")
    t.title("Third Window")
    fnt=('arial', 20, 'bold')
    l4=Label(t, text="Third Window")
    t4=Entry(t,font=fnt)
    l4.grid(row=0, column=1)
    t4.grid(row=0, column=2)
    t.mainloop()


fnt=('arial', 20, 'bold')
l4 = Label(text='Enter the name of the student')
t4 = Entry(font=fnt)
l4.grid(row=0, column=0)
t4.grid(row=0, column=1)


# ------------------
def calculate():
    global top
    top = Toplevel(root)
    top.geometry("600x300+50+50")
    l2 = Label(top,text='Enter the number ', font=fnt)
    t2 = Entry(top,font=fnt)
    l2.grid(row=0, column=0, padx=5, pady=5)
    t2.grid(row=0, column=1, padx=5, pady=5)
    b2 = Button(top, text="Calculate", command=thirdwindow)
    b2.grid(row=0, column=2, padx=5, pady=5)
    top.mainloop()
# --------------------------------
# All Controls
fnt=('arial',15,'bold')
l1 = Label(text='Enter the name',font=fnt)
t1 = Entry(font=fnt)
b1 = Button(text='child window',font=fnt,command=calculate)
# ---------------------------------
l1.grid(row=0, column=0, padx=5, pady=5)
t1.grid(row=1, column=0, padx=5, pady=5)
b1.grid(row=2, column=0, padx=5, pady=5)



root.mainloop()
