# Цвет заливки и цвет обводки
from tkinter import *
from tkinter import ttk

def draw_circle():
    fill_color = fill_color_entry_var.get()
    outline_color = outline_color_entry_var.get()
    canvas.create_oval(50, 50, 150, 150, outline=outline_color, fill=fill_color, width=5)

def draw_triangle():
    fill_color = fill_color_entry_var.get()
    outline_color = outline_color_entry_var.get()
    canvas.create_polygon(50, 150, 100, 50, 150, 150, outline=outline_color, fill=fill_color, width=5)

def draw_square():
    fill_color = fill_color_entry_var.get()
    outline_color = outline_color_entry_var.get()
    canvas.create_rectangle(50, 50, 150, 150, outline=outline_color, fill=fill_color, width=5)

def clear_canvas():
    canvas.delete("all")

def change_outline_color():
    color = bg_color_var.get()
    canvas.configure(bg=color)

# def bg_color():
#     color=bg_color_entry.get()
#     canvas.configure(bg=color)

color_options = ["Black", "Red", "Green", "Blue", "Yellow", "Purple",
                 "Brown", "White", "Gray", "Pink", "Tan", "Beige",
                 "Light Blue", "Teal", "Navy", "Olive", "Chartreuse",
                 "Lavender", "Maroon", "Orange", "Silver", "Gold"]

window = Tk()
window.title("Рисование фигур")
window.geometry("400x600")

canvas = Canvas(window, width=300, height=200)
canvas.pack()

# Метка и поле для ввода цвета заливки
Label(window, text="Цвет заливки:").pack()
fill_color_entry_var = StringVar()
fill_color_entry = ttk.OptionMenu(window, fill_color_entry_var, color_options[4], *color_options)
fill_color_entry.pack(pady=5)


# Метка и поле для ввода цвета обводки
Label(window, text="Цвет обводки:").pack()
outline_color_entry_var = StringVar()
outline_color_entry = ttk.OptionMenu(window, outline_color_entry_var, color_options[8], *color_options)
outline_color_entry.pack(pady=5)

circle_button = Button(window, text="Окружность", command=draw_circle)
circle_button.pack(pady=10)
triangle_button = Button(window, text="Треугольник", command=draw_triangle)
triangle_button.pack(pady=10)
square_button = Button(window, text="Квадрат", command=draw_square)
square_button.pack(pady=10)
clear_button = Button(window, text="Очистить", command=clear_canvas)
clear_button.pack(pady=10)

# Label(window, text="Цвет фона:").pack()
# bg_color_entry = Entry(window)
# bg_color_entry.pack(pady=5)
# bg_color_entry.insert(0, "black")
# bg_button=Button(window, text="Изменить цвет фона", command=bg_color)
# bg_button.pack()


bg_color_var = StringVar()
outline_color_menu = ttk.OptionMenu(window, bg_color_var, color_options[7], *color_options)
outline_color_menu.pack(pady=5)
button = Button(window, text="Изменить цвет фона", command=change_outline_color)
button.pack()



window.mainloop()


