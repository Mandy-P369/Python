from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def calculate_fare():
    # Get inputs
    passenger_class = cmb1.get()
    num_passengers = t_passengers.get()
    age_group = cmb3.get()
    
    # Validation
    if passenger_class not in ['Tier I', 'Tier II', 'Tier III']:
        messagebox.showerror("Error", "Select a valid class")
        return
    if not num_passengers.isdigit() or int(num_passengers) <= 0:
        messagebox.showerror("Error", "Enter a valid number of passengers")
        return
    num_passengers = int(num_passengers)
    
    # Step 1: Base fare
    if passenger_class == 'Tier I':
        base_fare = 5000
    elif passenger_class == 'Tier II':
        base_fare = 3000
    else:
        base_fare = 1000

    # Step 2: Discount rate
    if age_group == '<18':
        discount_rate = 0.5
    elif age_group == '>60':
        discount_rate = 0.4
    else:
        discount_rate = 0

    # Step 3 & 4: Total fare and discount
    total_fare = base_fare * num_passengers
    discount_total = base_fare * discount_rate * num_passengers

    # Step 5: Final amount
    final_amount = total_fare - discount_total

    # Update UI
    l4.config(text=f"{base_fare}")
    l8.config(text=f"{total_fare}")
    t_discount.delete(0, END)
    t_discount.insert(0, f"{discount_total}")
    l11.config(text=f"{final_amount}")

# GUI
top = Tk()
top.geometry('800x800+100+50')
top.title("Ticket Booking with Proper Calculation")
fnt = ('Arial', 15, 'bold')

Label(top, text='Ticket Center', font=('Arial', 20, 'bold')).pack(pady=10)

Label(top, text='Select Class:', font=fnt).pack(pady=5)
cmb1 = ttk.Combobox(top, values=['Tier I','Tier II','Tier III'], font=fnt)
cmb1.pack(pady=5)

Label(top, text='Number of Passengers:', font=fnt).pack(pady=5)
t_passengers = Entry(top, font=fnt)
t_passengers.pack(pady=5)

Label(top, text='Age Group:', font=fnt).pack(pady=5)
cmb3 = ttk.Combobox(top, values=['<18','18-60','>60'], font=fnt)
cmb3.pack(pady=5)

Label(top, text='Fare / Passenger:', font=fnt).pack(pady=5)
l4 = Label(top, font=fnt)
l4.pack(pady=5)

Label(top, text='Total Fare:', font=fnt).pack(pady=5)
l8 = Label(top, font=fnt)
l8.pack(pady=5)

Label(top, text='Discount:', font=fnt).pack(pady=5)
t_discount = Entry(top, font=fnt)
t_discount.pack(pady=5)

Label(top, text='Final Amount:', font=fnt).pack(pady=5)
l11 = Label(top, font=fnt)
l11.pack(pady=5)

Button(top, text='Calculate Fare', font=fnt, bg='black', fg='white', width=20, command=calculate_fare).pack(pady=20)

top.mainloop()
