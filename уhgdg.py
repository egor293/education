from tkinter import *
from tkinter import Tk
from tkinter import ttk,filedialog,colorchooser
from tkinter.messagebox import showinfo


with open('text2.txt','r') as file:
    file_text=file.read()

search = 'а'
count = 0

for text in file_text.split():
    if text == search:
        count+=1
print(f'{search} упоминается в произведении {count} раз')