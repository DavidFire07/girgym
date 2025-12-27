import tkinter as tk

def parentheses_checker(expression):
    stack = []
    for char in expression:
        if char == "(":
            stack.append("(")
        elif char == ")" :
            if not stack or stack[-1] != "(":
                return False
            stack.pop()
    
    return len(stack) == 0

def parentheses():
    data = list(entry.get())

    color_index = 0
    colors = ["red", "green", "blue", "yellow", "purple", "pink", "orange"]

    for tag in ["char", "status"]:
        canvas.delete(tag)
    
    display_text = ""
    index = 0
    if parentheses_checker(data):

        x = 10
        for char in data:
            if char == "(":
                canvas.create_text(x, 10, font=("Arial", 16), text=char, tags="char", fill=colors[index])
                index += 1
            elif char == ")":
                index -= 1
                canvas.create_text(x, 10, font=("Arial", 16), text=char, tags="char", fill=colors[index])
            else:
                canvas.create_text(x, 10, font=("Arial", 16), text=char, tags="char")
            
            x += 20

        display_text = "Current expression is correct!"

    else:
        display_text = "Current expression is incorrect!"
    
    canvas.create_text(140, 40, font=("Arial", 16), text=display_text, tags="status")
    

root = tk.Tk()
canvas = tk.Canvas(root, width=1000, height=400)
canvas.pack()

entry = tk.Entry(root, font=("Arial", 16), bg="light yellow")
entry.pack()

button = tk.Button(root, font=("Arial", 16), text="submit", command=parentheses)
button.pack()

root.mainloop()
