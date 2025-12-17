import tkinter as tk
root = tk.Tk()

canvas = tk.Canvas(root, height=500, width=500, bg="white")
canvas.pack()
#(a+b)-((a-b)*2)
user_input = input("Zadajte vyraz zo zatvorkami:")
farby = ["yellow","green","blue","brown","pink","purple"]
def farba():
    x = 100
    l_bracket = []
    r_bracket = []
    for index,pismeno in enumerate(user_input):
        if pismeno == "(":
            l_bracket.append(index)
        elif pismeno == ")":
            r_bracket.append(index)
    for index, pismeno in enumerate(user_input):
        if pismeno == "(":
            pass
        elif pismeno == ")":
            pass
        else:
            canvas.create_text(x,300, text=pismeno, fill="red")
            x += 20


def brackets_correct(expr):
    stack = []
    pairs = {')': '('}

    for ch in expr:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()

    return not stack
correction = brackets_correct(user_input)
def funkcia():
    lava_zatvorka = 0
    prava_zatvorka = 0
    for pismeno in user_input:
        if pismeno == "(":
            lava_zatvorka += 1
        elif pismeno == ")":
            prava_zatvorka += 1

    if lava_zatvorka == prava_zatvorka and correction == True:
        canvas.create_text(200,400, text="Zatvorkovanie je spravne")
        farba()
    else:
        canvas.create_text(200,400, text="Zatvorkovanie je nespravne")

funkcia()

root.mainloop()