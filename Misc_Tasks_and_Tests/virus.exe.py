import pyautogui
import random
import time
import string
import rotatescreen
from tkinter import *
from tkinter import ttk

screen=rotatescreen.get_primary_display()
start=screen.current_orientation

string_new=string.ascii_uppercase
string_new=''.join(random.sample(string_new,22))
for o in range(5):
    string_new+=string_new
#print(''.join(random.sample(string_new,500)))

    
def nuke_pc():
    for i in range(33):
        window=Tk()
        window.geometry('600x600')
        window.title('DIE_DIE_DIE_DIE_DIE_DIE_DIE_DIE_DIE_DIE_DIE_DIE_DIE_DIE_DIE_DIE_DIE')
        window.resizable(False,False)
        window.configure(bg='#FF0000')
        wondow.place(x=random.randint(0,1920),y=random.randint(0,1080))
        text=Label(window,text=(''.join(random.sample(string_new,500)))).place(x=0,y=0)
        for u in range(3):
            x=random.randint(0,1920)
            y=random.randint(0,1080)
            pyautogui.moveTo(x,y,0)
        a=abs((start-i*90)%360)
        screen.rotate_to(a)
        time.sleep(0)


#def sure():
#    window=Tk()
#    window.resizable(False,False)
#    window.configure(bg='#FF0000')
#    window.geometry('150x150')
#    label=Label(window,text=('ARE YOU SURE?! IT CAN NUKE YOUR PC!',)).place(x=200,y=200)
    

death=Tk()
death.title('DEATH')
death.geometry('1000x1000')
death.resizable(False,False)
death.configure(bg='#000000')
Button(text='KILL_PC',command=nuke_pc,background='#FF0000',activebackground='#000000',activeforeground='#000000').place(x=0,y=0,height=250,width=500)
Button(text='KILL_PC',command=nuke_pc,background='#FF0000',activebackground='#000000',activeforeground='#000000').place(x=0,y=250,height=250,width=500)
Button(text='KILL_PC',command=nuke_pc,background='#FF0000',activebackground='#000000',activeforeground='#000000').place(x=0,y=500,height=250,width=500)
Button(text='KILL_PC',command=nuke_pc,background='#FF0000',activebackground='#000000',activeforeground='#000000').place(x=0,y=750,height=250,width=500)
Button(text='KILL_PC',command=nuke_pc,background='#FF0000',activebackground='#000000',activeforeground='#000000').place(x=500,y=250,height=250,width=500)
Button(text='KILL_PC',command=nuke_pc,background='#FF0000',activebackground='#000000',activeforeground='#000000').place(x=500,y=500,height=250,width=500)
Button(text='KILL_PC',command=nuke_pc,background='#FF0000',activebackground='#000000',activeforeground='#000000').place(x=500,y=750,height=250,width=500)
Button(text='KILL_PC',command=nuke_pc,background='#FF0000',activebackground='#000000',activeforeground='#000000').place(x=500,y=0,height=250,width=500)

death.mainloop()
