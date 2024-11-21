from tkinter.font import names

import requests
import json
import pprint
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk

from pygame.examples.cursors import bitmap_cursor1

def update_b_label(event):
    code=b_combobox.get()
    name=currency_dict[code]
    b_label.config(text=name)


def update_cur_label(event):
    code=t_combobox.get()
    name=currency_dict[code]
    cur_label.config(text=name)

def exchange():
    cur_code=t_combobox.get()
    b_cur_code=b_combobox.get()

    if cur_code and b_cur_code:
        try:
            response = requests.get(f'https://v6.exchangerate-api.com/v6/1e889921444d2292c7202e8b/latest/{b_cur_code}')
            response.raise_for_status()
            data=response.json()
            if cur_code in data['conversion_rates']:
                exchange_rate=data['conversion_rates'][cur_code]
                c_name=currency_dict[cur_code]
                b_name=currency_dict[b_cur_code]
                mb.showinfo('Exchanges currency', f'Exchanges currency {exchange_rate:.2f} {c_name} for 1 {b_name}')
            else:
                mb.showerror('Error', f'Currency {cur_code} is not defined')
        except Exception as e:
            mb.showerror('Error', f'Happened problem: {e}')
    else:
        mb.showwarning('Attention!', 'Input another currency code')


window=Tk()
window.title('Exchanges currency')
window.geometry('400x200')

currency_dict = {
    'USD': 'US Dollar',
    'EUR': 'Euro',
    'JPY': 'Japanese Yen',
    'GBP': 'British Pound',
    'CAD': 'Canadian Dollar',
    'AUD': 'Australian Dollar',
    'CNY': 'Chinese Yuan',
    'RUB': 'Russian Ruble',
    'NZD': 'New Zealand Dollar'
}

Label(text='Choose base currency').pack(padx=10, pady=5)

b_combobox=ttk.Combobox(values=list(currency_dict.keys()))
b_combobox.pack()
b_combobox.bind("<<ComboboxSelected>>", update_b_label)
b_label=(ttk.Label())
b_label.pack()

Label(text='Choose code currency').pack(padx=10, pady=5)

t_combobox=ttk.Combobox(values=list(currency_dict.keys()))
t_combobox.pack()
t_combobox.bind("<<ComboboxSelected>>", update_cur_label)
# entery=Entry()
# entery.pack()

cur_label=(ttk.Label())
cur_label.pack()

Button(text='Get info', command=exchange).pack(padx=10, pady=5)





window.mainloop()
