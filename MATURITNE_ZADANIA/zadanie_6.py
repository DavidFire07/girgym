import tkinter as tk
root = tk.Tk()
canvas = tk.Canvas(root, height= 400, width=700,background="white")
canvas.pack()
parameters = []

with open("zadanie_6.txt","r") as f:
    for line in f:
         p = line.strip().split()
         parameters.append(p)

x1 = 55
x2 = 55
index = 0
canvas.create_line(x1,300,645,300,fill="white")

for i in parameters:
    if int(parameters[index][1]) != 0:
        y1 = 300 - int(parameters[index][1])
        x2 += int(parameters[index][0])
        canvas.create_rectangle(x1,y1,x2,300)
        x1 += int(parameters[index][0])
        index += 1
    elif int(parameters[index][1]) == 0:
        x2 += int(parameters[index][0])
        canvas.create_rectangle(x1,300,x2,300,outline="green")
        x1 += int(parameters[index][0])
        index += 1
def vyskovy_rozdiel():
    data = int(entry.get())
    x = 55

    canvas.delete("diff_line")

    for i in range(len(parameters) - 1):
        height1 = int(parameters[i][1])
        height2 = int(parameters[i+1][1])
        width = int(parameters[i][0])
        diff = abs(height1 - height2)

        x += width

        if diff == data:
            top = 300 - height1
            bottom = 300 - height2
            canvas.create_line(x, top, x, bottom, fill="red", width=2, tags="diff_line")

entry = tk.Entry()
entry.pack()
entry.insert(0,"")

button = tk.Button(text="vyskovy rozdiel",command=vyskovy_rozdiel)
button.pack()

root.mainloop()
