from tkinter import *
from random import *
from time import *

def key_pressed(event):
    global a
    global tmp
    sleep(0.1)
    for i in range(1, n):
        sleep(0.1)
        canvas.itemconfigure(cols[i], fill='blue')
        canvas.itemconfigure(cols[i-1], fill='blue')
        master.update()
        key = a[i]
        tmp = cols[i]
        j = i-1
        while j >=0 and key < a[j]:
            a[j+1] = a[j]
            canvas.itemconfigure(cols[j], fill='orange')
            canvas.itemconfigure(cols[j+1], fill='green')
            j -= 1
        a[j+1] = key
        cols[j+1] = tmp
        canvas.itemconfigure(cols[i], fill='orange')
        canvas.itemconfigure(cols[i-1], fill='orange')
        master.update()
    print(a)

def sdvig(j):
    canvas.move(cols[j+1], -wn, 0)

def replace_cols(j):
    global cols
    canvas.move(cols[j], wn, 0)
    canvas.move(cols[j+1], -wn, 0)
    cols[j], cols[j+1] = cols[j+1], cols[j]
    master.update()



    
n = int(input("Элементов в массиве: "))
a = [randint(1,1000) for i in range(n)]



print(a)
ww = 800
hh = 800
cols = []
wn = ww/n
master = Tk()
canvas = Canvas(master, height=hh, width=ww)
for i in range(n):
    cols.append(canvas.create_rectangle(wn*i, hh/1000*a[i], wn*i+ww/n, hh, fill="orange"))

canvas.pack()
master.title("Сортировка вставками")
master.bind("<KeyPress>", key_pressed) 
master.mainloop()
