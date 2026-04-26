import random

digits = [
[1,1,1, 1,0,1, 1,0,1, 1,0,1, 1,1,1],  # 0
[0,1,0, 1,1,0, 0,1,0, 0,1,0, 1,1,1],  # 1
[1,1,1, 0,0,1, 1,1,1, 1,0,0, 1,1,1],  # 2
[1,1,1, 0,0,1, 1,1,1, 0,0,1, 1,1,1],  # 3
[1,0,1, 1,0,1, 1,1,1, 0,0,1, 0,0,1],  # 4
[1,1,1, 1,0,0, 1,1,1, 0,0,1, 1,1,1],  # 5
[1,1,1, 1,0,0, 1,1,1, 1,0,1, 1,1,1],  # 6
[1,1,1, 0,0,1, 0,0,1, 0,0,1, 0,0,1],  # 7
[1,1,1, 1,0,1, 1,1,1, 1,0,1, 1,1,1],  # 8
[1,1,1, 1,0,1, 1,1,1, 0,0,1, 1,1,1],  # 9
]

input_size = 15
output_size = 10

w1 = [[random.uniform(-0.1, 0.1) for i in range(input_size)] for i in range(output_size)]
b1 = [[random.uniform(-0.1, 0.1) for i in range(in)]]


















import tkinter as tk

matrix = []

class DrawableGrid(tk.Frame):
    def __init__(self, parent, width, height, size=5):
        super().__init__(parent, bd=1, relief="sunken")
        self.width = width
        self.height = height
        self.size = size
        canvas_width = width*size
        canvas_height = height*size
        self.canvas = tk.Canvas(self, bd=0, highlightthickness=0, width=canvas_width, height=canvas_height)
        self.canvas.pack(fill="both", expand=True, padx=2, pady=2)

        for row in range(self.height):
            for column in range(self.width):
                x0, y0 = (column * size), (row*size)
                x1, y1 = (x0 + size), (y0 + size)
                self.canvas.create_rectangle(x0, y0, x1, y1,
                                             fill="white", outline="gray",
                                             tags=(self._tag(row, column),"cell" ))
        self.canvas.tag_bind("cell", "<B1-Motion>", self.paint)
        self.canvas.tag_bind("cell", "<1>", self.paint)

    def _tag(self, row, column):
        """Return the tag for a given row and column"""
        tag = f"{row},{column}"
        return tag

    def get_pixels(self):
        global matrix
        row = ""
        matrix = []
        for row in range(self.height):
            output = []
            for column in range(self.width):
                color = self.canvas.itemcget(self._tag(row, column), "fill")
                value = 1 if color == "black" else 0
                output.append(value)
            matrix.append(output)
        

    def paint(self, event):
        cell = self.canvas.find_closest(event.x, event.y)
        self.canvas.itemconfigure(cell, fill="black")
    



root = tk.Tk()

canvas = DrawableGrid(root, width=3, height=5, size=45)
b = tk.Button(root, text="Print Data", command=canvas.get_pixels)
b.pack(side="top")
canvas.pack(fill="both", expand=True)
root.mainloop()


