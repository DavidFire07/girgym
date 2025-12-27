import tkinter as tk

with open("ciernobiely_obrazok_1.txt", "r", encoding="utf-8") as file:
    header = file.readline().strip().split()
    widht = int(header[0])
    height = int(header[1])

    shades_count = {}

    for i in range(256):
        shades_count[i] = 0

    for _ in range(height):
        line = file.readline().strip()

        for i in range(widht):
            start = i * 2
            end = i * 2 + 2

            hex_code = line[start:end]
            shade = int(hex_code, 16)
            shades_count[shade] += 1


root = tk.Tk()

canvas = tk.Canvas(root, width=2*256, height=500)
canvas.pack()

for i in range(256):
    shade_count = shades_count[i]
    
    x1 = i * 2
    y1 = 500
    x2 = x1 + 2
    y2 = y1 - shade_count

    canvas.create_rectangle(x1, y1, x2, y2, fill="black")

root.mainloop()