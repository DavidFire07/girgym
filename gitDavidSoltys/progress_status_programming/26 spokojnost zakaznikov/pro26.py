import tkinter as tk

with open("spokojnost_2.txt", "r") as file:
    data = [line.strip().split() for line in file.readlines()]

table = {f"{i:02d}": 0 for i in range(24)}
total_negative_count = 0

for expression in data:
    if expression[1] == "nie":
        hour = expression[0][:2]
        table[hour] = table.get(hour, 0) + 1
        total_negative_count += 1

print(f"Total count of negative expressions: {total_negative_count}")
print()

negative_hour, negative_count = max(table.items(), key=lambda x: x[1])
print(f"Heighest negative count: {negative_count} during {negative_hour} hour")
print()

for hour, count in [(hour, count) for hour, count in table.items() if count != 0]:
    print(f"Negative count: {count} during {hour} hour")
print()

root = tk.Tk()

canvas = tk.Canvas(root, width=480, height=520)
canvas.pack()

for i in range(24):
    difference = 480 // 24
    if table[f"{i:02d}"] != 0:
        canvas.create_rectangle(difference * i, 480, difference * (i + 1), 480 - table[f"{i:02d}"], fill="red")
    else:
        canvas.create_line(difference * i, 480, difference * (i + 1) , 480, fill="black")
    canvas.create_text(difference * i, 485, text=f"{i:02d}", font=("Arial", 5))

root.mainloop()