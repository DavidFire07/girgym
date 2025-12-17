import tkinter, random
root = tkinter.Tk()

delenec = random.randint(11,20)
delitel = random.randint(2,9)

vysledok = delenec // delitel
zvysok = delenec % delitel

canvas = tkinter.Canvas(root,width=600, height=200, bg="white")
canvas.create_text(10,10,text=str(delenec)+":"+str(delitel)+"=", anchor="nw", font="Courier 30")

canvas.pack()
farby = ["red","green","blue"]
def over():
    if vysledok == int(entry.get()):
        txt = "spravne"
    else:
        txt = "nesprave"
    canvas.create_text(10,50,anchor="nw", text=txt, font= "Courier 30")
x = 10
for kruzok in range(delenec - zvysok):
    cn = (kruzok // delitel) % 3
    canvas.create_oval(x,100,x+20,120,fill=farby[cn],width=0)
    x += 30

x += 20
for i in range(zvysok):
    canvas.create_oval(x,100,x+20,120,fill="yellow", width=0)
    x += 30

entry = tkinter.Entry()
entry.pack()
button = tkinter.Button(text="Over", command= over)
button.pack()

root.mainloop()