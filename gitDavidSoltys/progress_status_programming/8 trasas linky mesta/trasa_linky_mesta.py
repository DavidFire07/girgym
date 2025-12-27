import tkinter as tk

with open("trasa_linky_mesta.txt", "r", encoding="utf-8") as file:
    color = file.readline().strip()
    stations = [line.strip() for line in file.readlines()]

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=200)
canvas.pack()

difference = 20

for station in stations:     

    if station != stations[-1]:    
        canvas.create_line(20 + difference, 180, 40 + difference, 180, fill=color)

    if station == stations[0] or station == stations[-1]:
        canvas.create_rectangle(10 + difference, 170, 30 + difference, 190, fill=color, outline="white")

    elif station[0] == "*":
        station = station[1:]
        canvas.create_oval(15 + difference, 175, 25 + difference, 185, fill="white", outline=color)

    else:
        canvas.create_oval(15 + difference, 175, 25 + difference, 185, fill=color, outline="white")

    canvas.create_text(20 + difference, 160, text=station, anchor="w", angle=60)
    difference += 20


root.mainloop()
