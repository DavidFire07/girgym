import tkinter as tk
odtiene = []
riadky = []
counter = 0

with open('zadanie_30.txt', 'r') as f:
    sirka, vyska = f.readline().split()
    for line in f.readlines():
        riadok = line.strip().split()
        riadky.extend(riadok)


for riadok in riadky:
    x = 0
    y = 2
    for pismeno in riadok:
        if counter % 2 == 0:
            odtiene.append(riadok[x:y])
            x += 2
            y += 2
            counter += 1
        else:
            counter += 1
            continue
odtien_cislo = []
for odtien in odtiene:
    odtien_cislo.append(int(odtien,16))

slovnik_odtienov = {str(i): 0 for i in range(0,256)}
for odtien in odtien_cislo:
    slovnik_odtienov[str(odtien)] += 1

maxi = [0]
for k,v in slovnik_odtienov.items():
    if v > maxi[0]:
        maxi.clear()
        maxi.append(v)

for k,v in slovnik_odtienov.items():
    if v == maxi[0]:
        print(f'Najcastejsie pouzity odtien sivej {k}')

print(f'Hodnoty obrazka - sirka: {sirka}, vyska: {vyska}, pocet bodov: {int(sirka) * int(vyska)}')

root = tk.Tk()
root.title('histogram frekvencie')
canvas = tk.Canvas(root, width=520,height=520,bg='white')
canvas.pack()

x = 5
canvas.create_line(0,500,520,500,fill='black')
for k,v in slovnik_odtienov.items():
    canvas.create_rectangle(x,500,x+2,500 - v,fill='black')
    x += 2

root.mainloop()