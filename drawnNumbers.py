from tkinter import ttk
from tkinter import *   


def draw(event):
    # Get current mouse coordinates
    x, y = event.x, event.y
    # Draw a small oval to simulate a brush stroke
    r = 2
    canvas.create_oval(x-r, y-r, x+r, y+r, fill="black", outline="black")


window = Tk()
frm = ttk.Frame(window, padding=10, width=150, height=200, )
frm.grid(rowspan=5, columnspan=3)

ttk.Button(text="Проверить").grid(column=1, row=4)

canvas = Canvas(window, height=150, width=150, bg="white")
canvas.grid(row=2, column=1)
canvas.bind("<B1-Motion>", draw)

window.mainloop()
