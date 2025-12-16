import tkinter as tk

hodiny = ['0' +str(i) for i in range(0,10) ]
hodiny_1 = [str(i) for i in range(10,24)]
hodiny.extend(hodiny_1)
hodiny_dict = {hodina : 0 for hodina in hodiny}

with open('zadanie_26_.txt','r') as f:
    for line in f.readlines():
        cast_riadku = line.strip().split()
        if cast_riadku[1] == 'nie':
            hodiny_dict[cast_riadku[0][0:2]] += 1

pocet_neg_vyjadreni = [v for k,v in hodiny_dict.items()]

print(f'Celkovy pocet negativnych vyjadreni {sum(pocet_neg_vyjadreni)}'+'\n')

for k,v in hodiny_dict.items():
    if v == max(pocet_neg_vyjadreni):
        print(f'Pocas {k} hodiny je najviac nespokojnych zakaznikov {v}'+'\n')

for k,v in hodiny_dict.items():
    if v != 0:
        print(f'Pocas {k} hodiny bolo {v} nespokojnych zakaznikov')

root = tk.Tk()
canvas = tk.Canvas(root,width=480,height=520,bg='white')
canvas.pack()

x = 10
x_1 = 0

canvas.create_line(0,500,480,500,fill='black',)
for k,v in hodiny_dict.items():
    canvas.create_text(x,510,text=k)
    x += 20
    canvas.create_rectangle(x_1,500,x_1 + 20,500 - v,fill='red',outline='black')
    x_1 += 20

root.mainloop()