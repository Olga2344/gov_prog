import requests
import json
import pprint
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk

def exchange():
    cur_code=combobox.get()
    if cur_code:
        try:
            response = requests.get('https://v6.exchangerate-api.com/v6/1e889921444d2292c7202e8b/latest/USD')
            response.raise_for_status()
            data=response.json()
            if cur_code in data['conversion_rates']:
                exchange_rate=data['conversion_rates'][cur_code]
                mb.showinfo('Exchanges currency', f'Exchanges currency {exchange_rate:.2f} {cur_code} for 1 USD')
            else:
                mb.showerror('Error', f'Currency {cur_code} is not defined')
        except Exception as e:
            mb.showerror('Error', f'Happened problem: {e}')
    else:
        mb.showwarning('Attention!', 'Input another currency code')


window=Tk()
window.title('Exchanges currency')
window.geometry('400x200')

Label(text='Choose code currency').pack(padx=10, pady=10)
cur_list= ['USD', 'EUR', 'JPY', 'GBP', 'CAD', 'AUD', 'CNY', 'RUB', 'NZD']
combobox=ttk.Combobox(values=cur_list)
combobox.pack(padx=10, pady=10)
# entery=Entry()
# entery.pack()

Button(text='Get info', command=exchange).pack(padx=10, pady=10)





window.mainloop()
