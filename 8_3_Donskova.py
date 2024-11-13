from tkinter import *
from tkinter import messagebox as mb
from tkinter import  simpledialog as sd
import datetime
import time
import pygame

t=0
def set():
    global t
    rem=sd.askstring('time', "input time in format hh.mm")
    if rem:
        try:
            hour=int(rem.split(':')[0])
            minuts=int(rem.split(':')[1])
            now=datetime.datetime.now()
            print(now)
            dt=now.replace(hour=hour, minute=minuts)
            print(dt)
            t=dt.timestamp()
            print(t)
        except Exception as e:
            mb.showerror('error', 'error')

def check():
    global t
    if t:
        now=time.time()
        if now>=t:
            play_sound()
            t=0
    window.after(10000,check)


window=Tk()
window.title("reminder")
label=Label(text="do reminder")
label.pack(pady=10)
set_button=Button(text="do reminder", command=set)
set_button.pack()
window.mainloop()