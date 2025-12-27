import tkinter as tk

inverted = False

def switch_display(canvas):
    global inverted
    inverted = not inverted
    canvas.delete("all")
    display_image(canvas, inverted)

def display_image(canvas, inverted):
    if inverted:
        color_1 = "white"
        color_2 = "black"
    else:
        color_1 = "black"
        color_2 = "white"


    with open("komprimatovany obrazok.txt", "r", encoding="utf-8") as file:
        header = file.readline().strip().split()
        width = int(header[0])
        height = int(header[1])

        canvas.config(width=width, height=height)

        line = [int(n) for n in file.readline().strip().split()]
        x_position = 0
        y_position = 0

        while line:
            x_position = 0
            for i, n in enumerate(line):

                if (i + 1) % 2 == 1:
                    color = color_1
                else: 
                    color = color_2
                
                canvas.create_rectangle(x_position, y_position, x_position + n, y_position, fill=color, outline="")
                x_position += n

            line = [int(n) for n in file.readline().strip().split()]
            y_position += 1
        
root = tk.Tk()

canvas = tk.Canvas(root)
canvas.pack(side="top")

button = tk.Button(root, text="negatív", font=("Arial", 12), command=lambda: switch_display(canvas))
button.pack(side="top")

display_image(canvas, inverted)

root.mainloop()