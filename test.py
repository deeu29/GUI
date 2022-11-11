from tkinter import *
from tkinter import ttk
 
def print():
    tott = float(totText.get())
    top = Toplevel()
    top.geometry("300x300")
    top.config(bg="white")
    l = Label(top, text='----------***----RECIEPT----***----------*-')
    l.pack()
    l.config(bg="white")
    heading = Label(top, text='\tItem\tPRICE\tQTY\tTOTAL')
    heading.pack()
    heading.config(bg="white")
 
    for child in listBox.get_children():
        item = (listBox.item(child, 'values')[0])
        price = float(listBox.item(child, 'values')[1])
        qty = float(listBox.item(child, 'values')[2])
        tot = float(listBox.item(child, 'values')[3])
        item1 = Label(top, text=f'{item}\t{price}\t{qty}\t{tot}')
        item1.config(bg="white")
        item1.pack()
 
    tot = Label(top, text=f'Total\t{tott}')
    tot.config(bg="white")
    tot.pack()
 
 
def show():
    tot = 0
    if (first.get()):
        price = int(a1.get())
        qty = int(a6.get())
        tot = int(price * qty)
        tempList = [['citrazene', a1.get(), a6.get(), tot]]
        tempList.sort(key=lambda e: e[1], reverse=True)
        for i, (item, price, qty, tot) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(item, price, qty, tot))
 
    if (second.get()):
        price = int(a2.get())
        qty = int(a7.get())
        tot = int(price * qty)
        tempList = [['Paracetemol', a2.get(), a7.get(), tot]]
        tempList.sort(key=lambda e: e[1], reverse=True)
        for i, (item, price, qty, tot) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(item, price, qty, tot))
 
    if (third.get()):
        price = int(a3.get())
        qty = int(a8.get())
        tot = int(price * qty)
        tempList = [['ORS', a3.get(), a8.get(), tot]]
        tempList.sort(key=lambda e: e[1], reverse=True)
        for i, (item, price, qty, tot) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(item, price, qty, tot))
 
    if (fourth.get()):
        price = int(a4.get())
        qty = int(a9.get())
        tot = int(price * qty)
        tempList = [['Dispirin', a4.get(), a9.get(), tot]]
        tempList.sort(key=lambda e: e[1], reverse=True)
 
        for i, (item, price, qty, tot) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(item, price, qty, tot))
 
    if (fifth.get()):
        price = int(a5.get())
        qty = int(a10.get())
        tot = int(price * qty)
        tempList = [['Vitamin C', a5.get(), a10.get(), tot]]
        tempList.sort(key=lambda e: e[1], reverse=True)
        for i, (item, price, qty, tot) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(item, price, qty, tot))
 
    sum1 = 0.0
    for child in listBox.get_children():
        sum1 += float(listBox.item(child, 'values')[3])
    totText.set(sum1)
 
 
base = Tk()
base.title("Medical Inventory System using Python")
base.geometry("1000x600")
global e1
global e2
global e3
global e4
global totText
global balText
 
totText = StringVar()
balText = IntVar()
 
Label(base, text="Medical Inventory System using Python", font="arial 22 bold" ,bg="white").place(x=5, y=10)
 
 
first = IntVar()
Checkbutton(base, text="citrazene", variable=first).place(x=10, y=50)
 
second = IntVar()
Checkbutton(base, text="Paracetemol", variable=second).place(x=10, y=80)
 
third = IntVar()
Checkbutton(base, text="ORS", variable=third).place(x=10, y=110)
 
fourth = IntVar()
Checkbutton(base, text="Dispirin", variable=fourth).place(x=10, y=140)
 
fifth = IntVar()
Checkbutton(base, text="Vitamin C", variable=fifth).place(x=10, y=170)
Label(base, text="Total").place(x=600, y=10)
 
a1 = Entry(base)
a1.place(x=140, y=50)
 
a2 = Entry(base)
a2.place(x=140, y=80)
 
a3 = Entry(base)
a3.place(x=140, y=110)
 
a4 = Entry(base)
a4.place(x=140, y=140)
 
a5 = Entry(base)
a5.place(x=140, y=170)
 
a6 = Entry(base)
a6.place(x=300, y=50)
 
a7 = Entry(base)
a7.place(x=300, y=80)
 
a8 = Entry(base)
a8.place(x=300, y=110)
 
a9 = Entry(base)
a9.place(x=300, y=140)
 
a10 = Entry(base)
a10.place(x=300, y=170)
 
tot = Label(base, text="", font="arial 22 bold", textvariable=totText)
tot.place(x=650, y=10)
 
Button(base, text="Add", command=show, height=3, width=13).place(x=10, y=220)
 
Button(base, text="Print", command=print, height=3, width=13).place(x=850, y=120)
cols = ('item', 'price', 'qty', 'total')
listBox = ttk.Treeview(base, columns=cols, show='headings')
 
for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=300)
 
 
base.mainloop()