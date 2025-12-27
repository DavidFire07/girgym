import tkinter as tk

def color_liness():
    canvas.delete('redline')
    height_limit =int(entry.get())
    for i, diff in enumerate(differences):
        if diff >= height_limit:
            bigger_height = max(buildings[i][1], buildings[i + 1][1])
            smaller_height = min(buildings[i][1], buildings[i + 1][1])
            if not smaller_height == 0:
                canvas.create_line(50 + x_positions[i], 500 - smaller_height, 50 + x_positions[i], 500 - bigger_height, fill='red', width=5, tag='redline')
            


with open('stavba_na_ulici.txt', 'r') as file:
    content = file.readlines()

buildings = []
for line in content:
    buildings.append(list(map(int, (line.strip()).split())))

differences = []
for i in range(len(buildings) - 1):
    diff = abs(buildings[i][1] - buildings[i + 1][1])
    differences.append(diff)

x_positions = []
for i, building in enumerate(buildings):
    if x_positions:
        x_positions.append(x_positions[i - 1] + building[0])
    else:
        x_positions.append(building[0])

root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=600, bg='white')
canvas.pack()

canvas.create_line(50, 500, 750, 500, width=2)

x_position = 50
for building in buildings:
    if building[1] == 0:
        canvas.create_line(x_position, 500, x_position + building[0], 500, fill='green', width=5)
        x_position += building[0]
    else:
        canvas.create_rectangle(x_position, 500, x_position + building[0], 500 - building[1], fill='gray')
        x_position += building[0]

entry = tk.Entry(root, borderwidth=2, background='light yellow')
entry.place(x=100, y=550)

button = tk.Button(root, text="Submit", command=color_liness)
button.place(x=230, y=550)

root.mainloop()