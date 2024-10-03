from tkinter import *
from tkinter import ttk

okno = Tk()
okno.title('О_О')
okno.geometry('300x300')
okno.resizable(False,False)
okno.configure(bg='#11025c')

def sus():
    window=Tk()
    window.geometry('200x200')
    window.title('тесла')
    window.resizable(False,False)
    window.configure(bg='#120263')
    text=Label(window,text='Никола Тесла').place(x=60,y=0)

def sus2():
    window=Tk()
    window.geometry('200x200')
    window.title('ньютон')
    window.resizable(False,False)
    window.configure(bg='#120263')
    text=Label(window,text='Исаак Ньютон').place(x=60,y=0)

def sus3():
    window=Tk()
    window.geometry('200x200')
    window.title('менделеев')
    window.resizable(False,False)
    window.configure(bg='#120263')
    text=Label(window,text='Дмитрий Менделеев').place(x=45,y=0)

def sus4():
    window=Tk()
    window.geometry('200x200')
    window.title('габен')
    window.resizable(False,False)
    window.configure(bg='#120263')
    text=Label(window,text='Габен Ньюэлл').place(x=60,y=0)

def sus5():
    window=Tk()
    window.geometry('200x200')
    window.title('ломоносов')
    window.resizable(False,False)
    window.configure(bg='#120263')
    text=Label(window,text='Михаил Ломоносов').place(x=45,y=0)

def sus6():
    window=Tk()
    window.geometry('200x200')
    window.title('мистур бист')
    window.resizable(False,False)
    window.configure(bg='#120263')
    text=Label(window,text='Мистур Бист').place(x=60,y=0)

    
Button(text='тесла',command=sus,background='#11025c',activebackground='#1a038f',activeforeground='#300ceb').place(x=0,y=0,height=100,width=150)
Button(text='ньютон',command=sus2,background='#11025c',activebackground='#1a038f',activeforeground='#300ceb').place(x=150,y=0,height=100,width=150)
Button(text='менделеев',command=sus3,background='#11025c',activebackground='#1a038f',activeforeground='#300ceb').place(x=0,y=100,height=100,width=150)
Button(text='габен',command=sus4,background='#11025c',activebackground='#1a038f',activeforeground='#300ceb').place(x=150,y=100,height=100,width=150)
Button(text='ломоносов',command=sus5,background='#11025c',activebackground='#1a038f',activeforeground='#300ceb').place(x=0,y=200,height=100,width=150)
Button(text='ученый',command=sus6,background='#11025c',activebackground='#1a038f',activeforeground='#300ceb').place(x=150,y=200,height=100,width=150)


okno.mainloop()



# если иван это найдет он лох
