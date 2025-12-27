import random as r
import string as s
import tkinter as tk
import tkinter.messagebox as ms

def create_egg():
    global x, y, oval, text, letter

    x = r.randint(0, 600)
    y = 30

    letter = r.choice(s.ascii_uppercase)

    oval = canvas.create_oval(x, y, x + 35, y + 45, width=3)
    text = canvas.create_text(x + 8, y + 23, text="", anchor="w", font=("Arial", 20, "bold"))

def falling():
    difference = 4

    x0, y0, x1, y1 = canvas.coords(oval)
    canvas.coords(oval, x0, y0 + difference, x1, y1 + difference)

    x0, y0 = canvas.coords(text)
    canvas.coords(text, x0, y0 + difference)

    if y1 > ((height // 3) * 2):
        canvas.itemconfig(text, text=letter)
    
    if y1 > 550:
        ms.showinfo("GAME OVER", "NO MORE PROBLEMS")
        root.destroy()
        return
    else:
        root.after(50, falling)


def on_press(event):
    global letter

    if event.char == letter.lower():
        canvas.delete("all")
        create_egg()


root = tk.Tk()

width = 600
height = 500

canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()
create_egg()
root.bind("<Key>", on_press)
falling()

root.mainloop()