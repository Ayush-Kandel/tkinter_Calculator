from tkinter import *

# displayes string in entry

def press(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number)) # adding two strings


# eqauls to function

def button_equal():
    cal = str(e.get())  # store value of entry in cal
    total = eval(cal)  # runs the python which is passed as an argument
    e.delete(0, END)  # delete the value in entry
    e.insert(0, total)  # inserts the value in entry


def clear_but():
    e.delete(0, END)  #clears the entry in the screen


root = Tk()
root.configure(bg='black')
root.title('Basic Calculator')

e = Entry(root, width=30, borderwidth=2, font=('arial', 40), bg='black', fg='cyan')
e.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=10,
    pady=10,
    ipady=5.5,
    )

#Buttons
button_1 = Button(
    root,
    text='1',
    font=('arial', 30),
    padx=30,
    pady=15,
    command=lambda : press(1),
    )
button_2 = Button(
    root,
    text='2',
    font=('arial', 30),
    padx=30,
    pady=15,
    command=lambda : press(2),
    )
button_3 = Button(
    root,
    text='3',
    font=('arial', 30),
    padx=30,
    pady=15,
    command=lambda : press(3),
    )
button_4 = Button(
    root,
    text='4',
    font=('arial', 30),
    padx=30,
    pady=15,
    command=lambda : press(4),
    )
button_5 = Button(
    root,
    text='5',
    font=('arial', 30),
    padx=30,
    pady=15,
    command=lambda : press(5),
    )
button_6 = Button(
    root,
    text='6',
    font=('arial', 30),
    padx=30,
    pady=15,
    command=lambda : press(6),
    )
button_7 = Button(
    root,
    text='7',
    font=('arial', 30),
    padx=30,
    pady=15,
    command=lambda : press(7),
    )
button_8 = Button(
    root,
    text='8',
    font=('arial', 30),
    padx=30,
    pady=15,
    command=lambda : press(8),
    )

button_9 = Button(
    root,
    text='9',
    font=('arial', 30),
    padx=30,
    pady=15,
    command=lambda : press(9),
    )
button_0 = Button(
    root,
    text='0',
    font=('arial', 30),
    padx=30,
    pady=15,
    command=lambda : press(0),
    )

button_add = Button(
    root,
    text='+',
    padx=30,
    pady=15,
    font=('arial', 30),
    command=lambda : press('+'),
    )
button_equal = Button(
    root,
    text='=',
    padx=30,
    pady=70,
    font=('arial', 30),
    command=button_equal,
    )
button_sub = Button(
    root,
    text='-',
    padx=34,
    pady=15,
    font=('arial', 30),
    command=lambda : press('-'),
    )
button_mul = Button(
    root,
    text='*',
    padx=33,
    pady=15,
    font=('arial', 30),
    command=lambda : press('*'),
    )
button_div = Button(
    root,
    text='/',
    padx=35,
    pady=15,
    font=('arial', 30),
    command=lambda : press('/'),
    )
button_exp = Button(
    root,
    text='^',
    padx=31,
    pady=15,
    font=('arial', 30),
    command=lambda : press('**'),
    )
button_clr = Button(
    root,
    text='AC',
    padx=110,
    pady=20,
    font=('arial', 25),
    command=clear_but,
    )
button_mod = Button(
    root,
    text='MOD',
    padx=15,
    pady=25,
    font=('arial', 20),
    command=lambda:press('%'),
    )

#placement
button_add.grid(row=1, column=0)
button_sub.grid(row=1, column=1)
button_mul.grid(row=1, column=2)
button_exp.grid(row=1, column=3)
button_div.grid(row=2, column=3)
button_mod.grid(row=3, column=3)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_0.grid(row=5, column=0)
button_clr.grid(row=5, column=1, columns = 2)
button_equal.grid(row=4, column=3, rows=2)
root.mainloop()  #closes