from logging import root
from tkinter import *
from PIL import ImageTk, Image, ImageGrab
from tkinter import filedialog as fd
from tkinter import messagebox as mb


def quit():
    window.destroy()

def clear():
    size_entry.delete(0, END)
    # size_entry.insert(0, 0)
    canvas.delete("all")
    canvas.configure(bg="White")

def change_pen_size():
    global pen_size
    try:
        pen_size = int(size_entry.get())
    except ValueError as e:
        mb.showerror('erorr', e)
def draw(event):
    try:
        change_pen_size()
        x,y=event.x, event.y
        canvas.create_oval(x,y,x+pen_size,y+pen_size, fill=pen_color, outline=pen_color)
    except Exception as e:
        mb.showerror('error', e)

def load_image():
    try:

        file_path=fd.askopenfilename(filetypes=[('Image files', '*.png;*.jpg;*.jpeg;*.bmp;*.gif')])
        if file_path:
            image=Image.open(file_path)
            image=image.resize((600,400))
            image_tk=ImageTk.PhotoImage(image)
            canvas.create_image(0,0,anchor=NW,image=image_tk )
            canvas.image=image_tk
    except Exception as e:
        mb.showerror('error', e)

def save_image():
    try:
        filepath=fd.asksaveasfilename(defaultextension='.png', filetypes=[('PNG files', '*.png')])
        if filepath:
            x = canvas.winfo_x()+canvas.winfo_width()/2
            y = canvas.winfo_y()+canvas.winfo_height()/2
            x1 = x + canvas.winfo_width()
            y1 = y + canvas.winfo_height()
            ImageGrab.grab().crop((x,y,x1,y1)).save(filepath)
            mb.showinfo('saved', 'image saved')
    except Exception as e:
        mb.showerror('error', e)

window=Tk()
window.title('painter')

pen_color='black'
color_options = ["Black", "Red", "Green", "Blue", "Yellow", "Purple",
                 "Brown", "White", "Gray", "Pink", "Tan", "Beige"]


canvas=Canvas(bg="Green", width=600, height=400)
canvas.pack()
canvas.bind('<B1-Motion>', draw)

for color in color_options:
    lbl=Label(bg=color, width=2,height=1)
    lbl.pack(side=LEFT)
    lbl.bind('<Button-1>', lambda e, c=color: globals().update(pen_color=c))
menu_bar=Menu(window,bg="Beige")
window.config(menu=menu_bar)
file_menu=Menu(menu_bar,tearoff=0,bg="Beige")
menu_bar.add_cascade(label='file', menu=file_menu)
file_menu.add_command(label='download', command=load_image)
file_menu.add_command(label='save', command=save_image)
file_menu.add_separator()
file_menu.add_command(label='quit', command=quit)

Label(window, text="pen size:").pack(side="left")
size_entry = Entry(window)
size_entry.pack(side="left",pady=5)
pen_size=size_entry.insert(0, 22)
size_button=Button(window, text="change size", command=change_pen_size)
size_button.pack(side="left")
clear_button=Button(window, text="clear", command=clear)
clear_button.pack(side="left")

window.mainloop()