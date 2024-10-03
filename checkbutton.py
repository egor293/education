from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

okno = Tk()
okno.title('okoshko')
okno.geometry('500x500')

enable = IntVar()

def check_func():
    result=('Мы выбрали')
    if dota.get():
        result=f'{result} dota'
    if cs.get():
        result=f'{result} cs'
    if sapper.get():
        result=f'{result} sapper'
    games.set(result)
#    if enable.get():
#        showinfo(title='Информация',message='Включили')
#    else:
#        showinfo(title='Информация',message='Выключили')


dota=IntVar()        
checkbutton=Checkbutton(text='Dota', variable=dota,command=check_func,)
checkbutton.place(x=50,y=0)

cs=IntVar()        
checkbutton1=Checkbutton(text='CS', variable=cs,command=check_func,)
checkbutton1.place(x=50,y=20)

sapper=IntVar()        
checkbutton2=Checkbutton(text='сапер', variable=sapper,command=check_func,)
checkbutton2.place(x=50,y=40)

games = StringVar()
label2=Label(textvariable=games)
label2.place(x=50,y=60)

#def comanda():
#    print(enable.get())
#label = Label(textvariable=enable)
#label.place(x=50,y=50)
#button=Button(text='Кнопка',command=comanda)
#button.place(x=50,y=100)

root.mainloop()
