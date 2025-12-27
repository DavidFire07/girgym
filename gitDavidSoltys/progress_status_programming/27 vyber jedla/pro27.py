import tkinter as tk

def store_data(food):
    with open("vyber_jedla.txt", "a") as file:
        file.write(f"{food}\n")

def green():
    number = entry.get()
    store_data(f"{number} g")

def red():
    number = entry.get()
    store_data(f"{number} r")

def blue():
    number = entry.get()
    store_data(f"{number} b")

def yellow():
    number = entry.get()
    store_data(f"{number} y")

colors = ["green", "red", "blue", "yellow"]
table_callables = {
    "green": green,
    "red": red,
    "blue": blue,
    "yellow": yellow,
}

root = tk.Tk()

label = tk.Label(root, text="CHOOSE A DISH", font=("Arial", 50))
label.grid(column=0, row=0)

frame = tk.Frame(root)
frame.grid(column=0, row=1)

for color in colors:
    button = tk.Button(frame, width=17, height=8, bg=color, command=table_callables[color])
    button.pack(side="left", padx=10, pady=10)

label = tk.Label(root, text="Enter student ID", font=("Arial", 12))
label.grid(column=0, row=2)

entry = tk.Entry(root,font=("Arial", 10))
entry.grid(column=0, row=3, pady=10)

root.mainloop()