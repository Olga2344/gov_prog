import time
from tkinter import *
import random
from tkinter import messagebox as mb

def move_ball(event):
    key=event.keysym
    x1,y1,x2,y2=canvas.coords(ball)
    if key=="Up" and y1>0:
        canvas.move(ball,0,-20)
    elif key=="Down" and y2<300:
        canvas.move(ball, 0, 20)
    elif key=="Left" and  x1>0:
        canvas.move(ball, -20,0)
    elif key=="Right" and x2<400:
        canvas.move(ball, 20,0)
    chek_coll()

def chek_coll():
    b=canvas.coords(ball)
    s=canvas.coords(sq)
    if b[2] >s[0] and b[0]<s[2] and b[3]>s[1] and b[1]<s[3]:
        move_sq()
        update_score()

def update_score():
    global score, start_time
    score+=1
    sq_labele.config(text=f"score: {score}")
    if score >=2:
        end_t=time.time()
        if end_t-start_time<10:
            mb.showinfo('Win', 'Win!!')
        else:
            mb.showinfo('Loose', 'time is missing(')
        if mb.askyesno("","one more time?"):
            score = 0
            sq_labele.config(text=f"score: {score}")
            start_time = time.time()
        else:
            window.destroy()

def move_sq():
    x1,y1,=random.randint(0,380),random.randint(0,280)
    x2,y2=x1+20,y1+20
    canvas.coords(sq,x1,y1,x2,y2)

window=Tk()
window.title('game')
window.geometry('400x330')
score=0
canvas=Canvas(width=400, height=300)
canvas.pack()
ball=canvas.create_oval(180,180,220,220, fill="orange")
sq=canvas.create_rectangle(150,150,170,170, fill="black")
sq_labele=Label(text=f"score: {score}")
sq_labele.pack()


start_time=time.time()
window.bind("<KeyPress>", move_ball)
window.focus_set()

window.mainloop()