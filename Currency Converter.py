import datetime
from tkinter import *
from tkinter.ttk import Combobox
import requests
from time import strftime


url = "https://api.exchangerate-api.com/v4/latest/USD"
curr = requests.get(url).json()
converter = curr['rates']

def timanddat():
    x = datetime.datetime.now()
    dat = x.strftime('%x')
    tim = x.strftime('%X')

    da.config(text=dat)
    ti.config(text=tim)

    da.after(1000, timanddat)
    ti.after(1000, timanddat)


def submi():
    global t
    cfrom = fromValue.get()
    fcurrency = from_currency.get()
    tcurrency = to_currency.get()

    if cfrom<0:
        t['text'] = "Put value Greater than 0"
        return None

    if fcurrency!="USD":
        amount = cfrom/converter[fcurrency]
    else:
        amount = round(cfrom/converter[fcurrency])

    amount = round((amount*converter[tcurrency]), 2)
    print(amount)
    t['text'] = amount



root = Tk()
root.title("Currency Converter")
root.geometry("500x200")

fromValue = IntVar()
from_currency = StringVar()
from_currency.set("USD")
to_currency = StringVar()
to_currency.set("INR")

Label(root, text="Welcome to Real Time Currency Converter", fg="blue", font="lucida 15 bold").pack(fill=X)

da = Label(root, bg="red")
ti = Label(root, bg="grey")

frm = Entry(root, textvariable=fromValue, width=23)
t = Label(root, text='', relief=RIDGE, width=20, fg='black', bg='white')

from_ = Combobox(root, values=list(converter.keys()), textvariable=from_currency)
to = Combobox(root, textvariable=to_currency, values=list(converter.keys()))

sub = Button(root, text="Convert", command=submi).place(x=210, y=160)

frm.place(x=70, y=80)
t.place(x=270, y=80)
from_.place(x=70, y=120)
to.place(x=270, y=120)
da.pack()
ti.pack()

timanddat()
root.mainloop()