import pyautogui
import random
import time
import string
import rotatescreen

#for i in range(100):
#    x=random.randint(600,700)
#    y=random.randint(600,700)
#    pyautogui.moveTo(x,y,0.01)
#    time.sleep(0.01)


#string_new=string.ascii_lowercase
#string_new=''.join(random.sample(string_new,22))
#print(string_new)

#number=int(input('введите число: '))
#time.sleep(1)
#for i in range(number):
#    pyautogui.typewrite(string_new)
#    pyautogui.press('Enter')


#text = 'FUNNY'
#print(f'{text}')
#print(f'{text:#<20}')
#print(f'{text:_>20}')
#print(f'{text:.^20}')


screen=rotatescreen.get_primary_display()
start=screen.current_orientation

for i in range(17):
    a=abs((start-i*90)%360)
    screen.rotate_to(a)
    time.sleep(0.2)
