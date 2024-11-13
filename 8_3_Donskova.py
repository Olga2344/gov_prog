from tkinter import *
from tkinter import messagebox as mb
from tkinter import  simpledialog as sd
import datetime
import time
import pygame

t=0
music=False

def set():
    global t
    rem=sd.askstring('time', "input time in format hh.mm")
    if rem:
        try:
            hour=int(rem.split(':')[0])
            minuts=int(rem.split(':')[1])
            now=datetime.datetime.now()
            dt=now.replace(hour=hour, minute=minuts, second=0, microsecond=0)
            t=dt.timestamp()
            label.config(text=f"reminder: {hour:02}:{minuts:02}")

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
def stop_m():
    global music
    if music:
        pygame.mixer.music.stop()
        music=False
    label.config(text="set new reminder")

def play_sound():
    global music
    music=True
    pygame.mixer.init()
    pygame.mixer.music.load('r.mp3')
    pygame.mixer.music.play()

window=Tk()
window.title("reminder")
label=Label(text="do reminder")
label.pack(pady=10)
set_button=Button(text="do reminder", command=set)
set_button.pack(pady=10)
stop_b=Button(text="stop music", command=stop_m)
stop_b.pack(pady=10)

check()
window.mainloop()