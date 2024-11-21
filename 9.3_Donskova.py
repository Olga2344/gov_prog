import requests
import json
import pprint
from tkinter import *
from tkinter import messagebox as mb

def exchange():



window=Tk()
window.title('Exchanges currency')
window.geometry('400x200')

Label(text='Input code currency').pack(padx=10, pady=10)

entery=Entry()
entery.pack()

Button(text='Get info', command=exchange).pack(padx=10, pady=10)





window.mainloop()





result = requests.get('https://v6.exchangerate-api.com/v6/1e889921444d2292c7202e8b/latest/USD')
data= json.loads(result.text)
p=pprint.PrettyPrinter(indent=2)
p.pprint(data)