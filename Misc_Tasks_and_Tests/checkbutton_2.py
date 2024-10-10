from tkinter import *
from tkinter import ttk

screen = Tk()
screen.title('Приложение')
screen.geometry('400x200')

def btn_click_lesson():
    window=Tk()
    window.title('запись')
    window.geometry('400x200')
    text=Label(window,text='запишитесь на мастер класс')
    text.place(x=150,y=0)
    entry = Entry(window)
    entry.place(x=0,y=20)
    btn=Button(window,text='ваше имя')
    btn.place(x=100,y=20)
    Button(window,text='Закрыть',command=lambda: window.destroy()).place(x=125,y=50)
    
def btn_click():
    window=Tk()
    window.title('создание')
    window.geometry('400x200')
    text=Label(window,text='создайте мастер класс')
    text.place(x=150,y=0)
    entry = Entry(window)
    entry.place(x=0,y=20)
    btn=Button(window,text='Название мастер класса')
    btn.place(x=100,y=20)
    Button(window,text='Закрыть',command=lambda: window.destroy()).place(x=125,y=50)

Button(text='Записаться на мастер класс',command=btn_click_lesson).place(x=120,y=0)
Button(text='Создать мастер класс',command=btn_click).place(x=120,y=25)
Button(text='Закрыть',command=lambda: window.destroy()).place(x=344,y=0)
screen.mainloop()
