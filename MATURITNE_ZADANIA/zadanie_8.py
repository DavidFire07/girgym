
import tkinter as tk

zastavky = []

root = tk.Tk()
canvas = tk.Canvas(root, width= 600, height=500, bg='white')
canvas.pack()

with open('zadanie_8.txt','r') as f:
    farba = f.readline()
    for line in f.readlines():
        casti = line.strip().split(' ')
        zastavky.append(' '.join(casti[:]))


canvas.create_line(50,300,475,300, fill=farba.strip())
canvas.create_rectangle(40,295,50,305, fill=farba.strip())
canvas.create_rectangle(475,295,485,305,fill=farba.strip())
x_1 = 60
x_2 = 65
y_1 = 297
y_2 = 302
y = 280
x = 70
counter_1 = 0
counter_2 = 20
for index,zastavka in enumerate(zastavky):
    if index == counter_1:
        canvas.create_text(50,y,text=zastavka, anchor= 'sw', angle=80, font=('Arial',7))
        continue
    if index == counter_2:
        canvas.create_text(500, y, text=zastavka, anchor='sw', angle=80, font=('Arial', 7))
        continue
    if zastavka[0] == '*':
        canvas.create_rectangle(x_1, y_1, x_2, y_2, fill='white', outline=farba.strip())
        canvas.create_text(x, y, text=''.join(zastavka[1:]), anchor='sw', angle=80, font=('Arial', 7))
        x_1 += 22
        x_2 += 22
        x += 22
    else:
        canvas.create_rectangle(x_1,y_1,x_2,y_2,fill=farba.strip(),outline=farba.strip())
        canvas.create_text(x,y, text=zastavka,anchor='sw',angle=80, font=('Arial',8))
        x_1 += 22
        x_2 += 22
        x += 23






root.mainloop()
