import tkinter as tk
root = tk.Tk()
canvas = tk.Canvas(root,width=600,height=400,bg='white')
canvas.pack()

with open('zadanie_27.txt','w') as f:
    pass
def klik(event):
    if y_1 <= event.y <= y_2:
        if 0 <= event.x <= 150:
            if entry.get():
                with open('zadanie_27.txt','a') as f:
                    f.write(entry.get()+' '+'z'+'\n')
        elif 151 <= event.x <= 300:
            if entry.get():
                with open('zadanie_27.txt','a') as f:
                    f.write(entry.get()+' '+'c'+'\n')
        elif 301 <= event.x <= 450:
            if entry.get():
                with open('zadanie_27.txt','a') as f:
                    f.write(entry.get()+' '+'m'+'\n')
        elif 451 <= event.x <= 600:
            if entry.get():
                with open('zadanie_27.txt','a') as f:
                    f.write(entry.get()+' '+'o'+'\n')

entry = tk.Entry()
entry.insert(0,'kod stravnika')
entry.pack()

y_1 = 150
y_2 = 300
x = 0
canvas.create_text(300,100,text='Vyber jedla',fill='red',font=('Arial',20))
zelene = canvas.create_rectangle(x, y_1, x+150, y_2, fill="green", outline="black")
x += 150
cervene = canvas.create_rectangle(x, y_1,x+150, y_2, fill="red", outline="black")
x += 150
modre = canvas.create_rectangle(x, y_1,x+150, y_2, fill="blue", outline="black")
x += 150
oranzove = canvas.create_rectangle(x, y_1,x+150, y_2, fill="orange", outline="black")
canvas.bind("<Button-1>", klik)

root.mainloop()