from tkinter import *
from tkinter import Tk
from tkinter import ttk,filedialog,colorchooser
from tkinter.messagebox import showinfo

#with open('text.txt','w') as file:
#    file.write('hello')

#with open('text.txt','r') as file:
#    print(file.read())

okno = Tk()
okno.title('DonRobot')
okno.geometry('400x300')

text_window = Text()
text_window.place(x=0,y=0,width=400,height=200)

def open_file():
#    file_open = filedialog.askopenfilename()
#    if file_open != '':
#       with open('text.txt','r',encoding='utf=8') as file:
#           text = file.read()
#           text_window.delete('1.0', END)
#           text_window.insert('1.0', text)

        with open('text.txt','r',encoding='utf=8') as file:
            text = file.read()
            text_window.delete('1.0', END)
            text_window.insert('1.0', text)
            #text_window.delete()

def save_file():
    text=text_window.get('1.0', END)
    with open('text.txt','w',encoding='utf=8') as file:
        file.write(text)

def change_color():
    color=colorchooser.askcolor(initialcolor='black')
    text_window['foreground']=color[1]


ttk.Button(text='Открыть Файл',command = open_file).place(x=100,y=200)
ttk.Button(text='Сохранить файл',command = save_file).place(x=200,y=200)
ttk.Button(text='Выбрать Цвет',command = change_color).place(x=150,y=230)


okno.mainloop()
