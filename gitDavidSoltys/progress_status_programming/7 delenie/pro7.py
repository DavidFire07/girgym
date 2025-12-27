import tkinter as tk
import random as r

def over():
    answer = delenec // delitel
    remainder = delenec % delitel
    colors = ['red', 'green', 'blue']

    if int(entry.get()) == answer:
        txt = 'SPRAVNE'
    else:
        txt = 'NESPRAVNE'
    canvas.create_text(10, 50, text=txt, anchor='nw', font='Courier 30')

    x = 10
    for i in range(delenec - remainder):
        color_num = (i // delitel) % 3
        canvas.create_oval(x, 100, x + 20, 120, fill=colors[color_num], width=0)
        x += 30

    x += 20
    for i in range(remainder):
        canvas.create_oval(x, 100, x + 20, 120, fill='yellow', width=0)
        x += 30

delenec = r.randint(11, 20)
delitel = r.randint(2, 9)

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=200, bg='white')
canvas.pack()

canvas.create_text(10, 10, text=f'{delenec} : {delitel} =', font='Courier 30', anchor='nw')

entry = tk.Entry()
entry.pack()

button = tk.Button(text='Over', command=over)
button.pack()

root.mainloop()