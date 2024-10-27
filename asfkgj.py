from tkinter import *
from tkinter import ttk
window=Tk()
window.geometry('500x430')
window.resizable(False,False)
window.title('программа для отслеживания привычек')
privichki={}
def main_show():
    window1=Tk()
    window1.title('ваши привычки')
    window1.geometry('300x300')
    window1.resizable(False,False)
def main_add():
    window1=Tk()
    window1.title('добавление привычки')
    window1.geometry('300x300')
    window1.resizable(False,False)
    ttk.Entry(window1,text='название привычки').pack(anchor=NW,padx=6,pady=6)
    Button(window1,text='подтвердить',command=entry_get1).place(x=135,y=5,width=80,height=22)
def entry_get1():
    privichki[Entry.get()]=0
    print(privichki)
def main_delete():
    window1=Tk()
    window1.title('удаление привычки')
    window1.geometry('300x300')
    window1.resizable(False,False)
    ttk.Entry(window1,text='название привычки').pack(anchor=NW,padx=6,pady=6)
    Button(window1,text='подтвердить',command=entry_get).place(x=135,y=5,width=80,height=22)
def entry_get():
    a=Entry.get()
    if a in privichki:
        del privichki[Entry.get()]
        print(privichki)
def main_tasks():
    window1=Tk()
    window1.title('выполнение привычки')
    window1.geometry('300x300')
    window1.resizable(False,False)

Button(text='ваши привычки',command=main_show).place(x=175,y=0,height=100,width=150)
Button(text='добавление привычки',command=main_add).place(x=175,y=110,height=100,width=150)
Button(text='удаление привычки',command=main_delete).place(x=175,y=220,height=100,width=150)
Button(text='выполнение привычки',command=main_delete).place(x=175,y=330,height=100,width=150)


window.mainloop()