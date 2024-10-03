from tkinter import *
from tkinter import Tk
from tkinter import ttk,filedialog,colorchooser
from tkinter.messagebox import showinfo

# with open('text.txt','w',encoding='utf8') as file:
#    file.write('privet')

with open('text2.txt','r') as file:
#    print(file.read())
    file_text=file.read()

if 'Гнилотерки' in file_text:
    print('yes')
else:
    print('no')