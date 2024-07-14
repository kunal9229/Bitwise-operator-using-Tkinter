# Install Pillow, Pillow-PIL, PillowImage module manually

import tkinter
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import sqlite3

conn = sqlite3.connect('history.db')
conn.execute(
    """CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    operator varchar(10),
    num1 int,
    num2 int, 
    result int
)""")
conn.commit()
conn.close()

window = Tk()
window.title("Python Project")
window.geometry('550x300')
window.iconbitmap('images/icon.ico')


def about():
    window3 = Toplevel(window)
    window3.title("About")
    window3.geometry('400x380')
    window3.iconbitmap('images/icon.ico')
    Label(window3, text="Contributor", font='Helvetica 18 bold underline').place(x=170, y=10, anchor=CENTER)
    Label(window3, text="These student from CSE(B.Tech) Second Year has made this project", font='Arial 10 bold',
          wraplength=350, justify=LEFT).place(x=10, y=320)

    def dev(images, image_x, images_y, regno, regno_x, regno_y, name, name_x, name_y, rollno, rollno_x, rollno_y):
        img = Image.open(images)
        img = img.resize((80, 80), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)
        panel = Label(window3, image=img)
        panel.image = img
        panel.place(x=image_x, y=images_y)
        Label(window3, text="Registration Number: " + str(regno)).place(x=regno_x, y=regno_y)
        Label(window3, text="Name: " + name).place(x=name_x, y=name_y)
        Label(window3, text="Roll Number: " + str(rollno)).place(x=rollno_x, y=rollno_y)

    dev("images/lucky.png", 10, 40, 12203018, 100, 45, "Taorem Lucky Singh", 100, 65, 26, 100, 85)
    dev("images/kunal.jpeg", 10, 130, 12202896, 100, 135, "Kunal Yadav", 100, 155, 22, 100, 175)
    dev("images/aman.jpg", 10, 220, 12202682, 100, 225, "Aman Singh", 100, 245, 2, 100, 265)


menubar = Menu(window)
file = Menu(menubar, tearoff=0)
file.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=file)
help = Menu(menubar, tearoff=0)
help.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=help)

window.config(menu=menubar)

num1 = IntVar()
num2 = IntVar()

logic_operator = IntVar()

label1 = Label(window, bg='white', text='Number 1:', borderwidth=1, relief="solid")
label1.grid(padx=(10, 0), row=0, column=0, ipadx=10, ipady=5)
textbox1 = Entry(window, textvariable=num1, borderwidth=1, relief="solid")
textbox1.grid(row=0, column=1, ipadx=10, ipady=5)

label2 = Label(window, bg='white', text='Number 2:', borderwidth=1, relief="solid")
label2.grid(row=0, column=3, ipadx=10, ipady=5)
textbox2 = Entry(window, textvariable=num2, borderwidth=1, relief="solid")
textbox2.grid(row=0, column=4, ipadx=10, ipady=5)

radio1 = Radiobutton(text='AND', value=1, variable=logic_operator)
radio1.grid(row=1, column=1)

radio2 = Radiobutton(text='OR', value=2, variable=logic_operator)
radio2.grid(row=1, column=2)

radio3 = Radiobutton(text='NOT', value=3, variable=logic_operator)
radio3.grid(row=2, column=1)

radio4 = Radiobutton(text='XOR', value=4, variable=logic_operator)
radio4.grid(row=2, column=2)


def flip(c):
    return '1' if (c == '0') else '0'


def decimalToBinary(n):
    s1 = bin(n).replace('0b', '')
    return s1


def onesCompliment(n):
    binary_number = bin(n)
    x = ''
    for i in range(len(binary_number[2:])):
        if binary_number[i + 2] == '0':
            x = x + '1'
        if binary_number[i + 2] == '1':
            x = x + '0'
    return x



def calc():
    conn = sqlite3.connect('history.db')
    x = num1.get()
    y = num2.get()
    logic = logic_operator.get()
    if logic == 1:
        result.config(text='Result is: ' + str(int(decimalToBinary(x & y), 2)))
        conn.execute(
            "INSERT INTO history (operator,num1,num2,result) VALUES ('AND',?,?,?)",
            (x, y, str(int(decimalToBinary(x & y), 2))))
    elif logic == 2:
        result.config(text='Result is: ' + str(int(decimalToBinary(x | y), 2)))
        conn.execute(
            "INSERT INTO history (operator,num1,num2,result) VALUES ('OR',?,?,?)",
            (x, y, str(int(decimalToBinary(x | y), 2))))
    elif logic == 3:
        result.config(text='Result is: ' + str(int(onesCompliment(x), 2)))
        conn.execute(
            "INSERT INTO history (operator,num1,num2,result) VALUES ('NOT',?,'-',?)",
            (x, str(int(onesCompliment(x), 2))))
    else:
        result.config(text='Result is: ' + str(int(decimalToBinary(x ^ y), 2)))
        conn.execute(
            "INSERT INTO history (operator,num1,num2,result) VALUES ('XOR',?,?,?)",
            (x, y, str(int(decimalToBinary(x ^ y), 2))))
    cursor = conn.cursor()
    cursor.execute("select operator, num1,num2,result from history order by id desc")
    rows = cursor.fetchone()
    print(rows)
    tree.insert("", tkinter.END, values=rows)
    conn.close()


def clear_all():
    for item in tree.get_children():
        tree.delete(item)


def explanation():
    window2 = Toplevel(window)
    window2.title("Explanation")
    window2.geometry('550x300')
    window2.iconbitmap('images/icon.ico')

    x = num1.get()
    y = num2.get()
    logic = logic_operator.get()
    lab1 = Label(window2, bg='white', text='Number 1:', borderwidth=1, relief="solid")
    lab1.grid(padx=(10, 0), row=0, column=0, ipadx=10, ipady=5)
    lab1 = Label(window2, bg='white', text=str(x), borderwidth=1, relief="solid")
    lab1.grid(padx=(10, 0), row=0, column=1, ipadx=10, ipady=5)

    lab3 = Label(window2, bg='white', text='Binary:', borderwidth=1, relief="solid")
    lab3.grid(padx=(10, 0), row=0, column=4, ipadx=10, ipady=5)
    lab3 = Label(window2, bg='white', text=str(decimalToBinary(x)), borderwidth=1, relief="solid")
    lab3.grid(padx=(10, 0), row=0, column=5, ipadx=10, ipady=5)

    Label(window2).grid(row=2)
    Label(window2).grid(row=4)
    if logic == 1:
        lab2 = Label(window2, bg='white', text='Number 2:', borderwidth=1, relief="solid")
        lab2.grid(padx=(10, 0), row=1, column=0, ipadx=10, ipady=5)
        lab2 = Label(window2, bg='white', text=str(y), borderwidth=1, relief="solid")
        lab2.grid(padx=(10, 0), row=1, column=1, ipadx=10, ipady=5)

        lab4 = Label(window2, bg='white', text='Binary:', borderwidth=1, relief="solid")
        lab4.grid(padx=(10, 0), row=1, column=4, ipadx=10, ipady=5)
        lab4 = Label(window2, bg='white', text=str(decimalToBinary(y)), borderwidth=1, relief="solid")
        lab4.grid(padx=(10, 0), row=1, column=5, ipadx=10, ipady=5)

        lab5 = Label(window2, bg='white', text='AND:', borderwidth=1, relief="solid")
        lab5.grid(padx=(10, 0), row=3, column=4, ipadx=10, ipady=5)
        lab5 = Label(window2, bg='white', text=str(decimalToBinary(x & y)), borderwidth=1, relief="solid")
        lab5.grid(padx=(10, 0), row=3, column=5, ipadx=10, ipady=5)

        lab6 = Label(window2, bg='white', text='Decimal Result:', borderwidth=1, relief="solid")
        lab6.grid(padx=(10, 0), row=5, column=2, ipadx=10, ipady=5)
        lab6 = Label(window2, bg='white', text=str(int(decimalToBinary(x & y), 2)), borderwidth=1, relief="solid")
        lab6.grid(padx=(10, 0), row=5, column=3, ipadx=10, ipady=5)

        Label(window2, text="*Note: if both are 1 then 1 else 0!").place(
            relx=0.0,
            rely=1.0,
            anchor=SW)
    elif logic == 2:
        lab2 = Label(window2, bg='white', text='Number 2:', borderwidth=1, relief="solid")
        lab2.grid(padx=(10, 0), row=1, column=0, ipadx=10, ipady=5)
        lab2 = Label(window2, bg='white', text=str(y), borderwidth=1, relief="solid")
        lab2.grid(padx=(10, 0), row=1, column=1, ipadx=10, ipady=5)

        lab4 = Label(window2, bg='white', text='Binary:', borderwidth=1, relief="solid")
        lab4.grid(padx=(10, 0), row=1, column=4, ipadx=10, ipady=5)
        lab4 = Label(window2, bg='white', text=str(decimalToBinary(y)), borderwidth=1, relief="solid")
        lab4.grid(padx=(10, 0), row=1, column=5, ipadx=10, ipady=5)

        lab5 = Label(window2, bg='white', text='OR:', borderwidth=1, relief="solid")
        lab5.grid(padx=(10, 0), row=3, column=4, ipadx=10, ipady=5)
        lab5 = Label(window2, bg='white', text=str(decimalToBinary(x | y)), borderwidth=1, relief="solid")
        lab5.grid(padx=(10, 0), row=3, column=5, ipadx=10, ipady=5)

        lab6 = Label(window2, bg='white', text='Decimal Result:', borderwidth=1, relief="solid")
        lab6.grid(padx=(10, 0), row=5, column=2, ipadx=10, ipady=5)
        lab6 = Label(window2, bg='white', text=str(int(decimalToBinary(x | y), 2)), borderwidth=1, relief="solid")
        lab6.grid(padx=(10, 0), row=5, column=3, ipadx=10, ipady=5)

        Label(window2, text="*Note: if there is 1 on either side then 1 else 0!").place(
            relx=0.0,
            rely=1.0,
            anchor=SW)
    elif logic == 3:
        lab5 = Label(window2, bg='white', text='NOT:', borderwidth=1, relief="solid")
        lab5.grid(padx=(10, 0), row=3, column=4, ipadx=10, ipady=5)
        lab5 = Label(window2, bg='white', text=str(onesCompliment(x)), borderwidth=1, relief="solid")
        lab5.grid(padx=(10, 0), row=3, column=5, ipadx=10, ipady=5)

        lab6 = Label(window2, bg='white', text='Decimal Result:', borderwidth=1, relief="solid")
        lab6.grid(padx=(10, 0), row=5, column=2, ipadx=10, ipady=5)
        lab6 = Label(window2, bg='white', text=str(int(onesCompliment(x), 2)), borderwidth=1, relief="solid")
        lab6.grid(padx=(10, 0), row=5, column=3, ipadx=10, ipady=5)

        Label(window2, text="*Note: NOT bitwise operator is the 1's compliment of the given Binary Digits!").place(
            relx=0.0,
            rely=1.0,
            anchor=SW)
    else:
        lab2 = Label(window2, bg='white', text='Number 2:', borderwidth=1, relief="solid")
        lab2.grid(padx=(10, 0), row=1, column=0, ipadx=10, ipady=5)
        lab2 = Label(window2, bg='white', text=str(y), borderwidth=1, relief="solid")
        lab2.grid(padx=(10, 0), row=1, column=1, ipadx=10, ipady=5)

        lab4 = Label(window2, bg='white', text='Binary:', borderwidth=1, relief="solid")
        lab4.grid(padx=(10, 0), row=1, column=4, ipadx=10, ipady=5)
        lab4 = Label(window2, bg='white', text=str(decimalToBinary(y)), borderwidth=1, relief="solid")
        lab4.grid(padx=(10, 0), row=1, column=5, ipadx=10, ipady=5)

        lab5 = Label(window2, bg='white', text='XOR:', borderwidth=1, relief="solid")
        lab5.grid(padx=(10, 0), row=3, column=4, ipadx=10, ipady=5)
        lab5 = Label(window2, bg='white', text=str(decimalToBinary(x ^ y)), borderwidth=1, relief="solid")
        lab5.grid(padx=(10, 0), row=3, column=5, ipadx=10, ipady=5)

        lab6 = Label(window2, bg='white', text='Decimal Result:', borderwidth=1, relief="solid")
        lab6.grid(padx=(10, 0), row=5, column=2, ipadx=10, ipady=5)
        lab6 = Label(window2, bg='white', text=str(int(decimalToBinary(x ^ y), 2)), borderwidth=1, relief="solid")
        lab6.grid(padx=(10, 0), row=5, column=3, ipadx=10, ipady=5)

        Label(window2, text="*Note: If both are different then 1 else 0").place(
            relx=0.0,
            rely=1.0,
            anchor=SW)


button1 = Button(window, bg='white', command=calc, text='Result')
button1.grid(row=3, column=1, padx=5, pady=10)

button2 = Button(window, bg='white', command=explanation, text='Explanation')
button2.grid(row=3, column=2, padx=5, pady=10)

result = Label(window, bg='white', text='Result is:', borderwidth=1, relief="solid")
result.grid(row=4, column=0, ipadx=10, ipady=5)
Label(window, text="*Note: Only the First Number will be selected if the bitwise operation is NOT!").place(relx=0.0,
                                                                                                           rely=1.0,
                                                                                                           anchor=SW)

frame = Frame(window)
frame.place(x=330, y=130)

tree = ttk.Treeview(frame, columns=("1", "2", "3", "4", "5"), height=5, show="headings")
tree.grid()

tree.heading(1, text="Operator")
tree.heading(2, text="NO.1")
tree.heading(3, text="NO.2")
tree.heading(4, text="Result")
tree.heading(5, text="")

tree.column(1, width=60, anchor=CENTER)
tree.column(2, width=40, anchor=CENTER)
tree.column(3, width=40, anchor=CENTER)
tree.column(4, width=50, anchor=CENTER)
tree.column(5, width=10)

scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
scroll.place(x=182, height=130,width=20)

tree.configure(yscrollcommand=scroll.set)
Label(window, text="History:").place(x=280, y=125)
Button(window, text="Clear History", command=clear_all).place(x=245, y=230)

window.mainloop()
