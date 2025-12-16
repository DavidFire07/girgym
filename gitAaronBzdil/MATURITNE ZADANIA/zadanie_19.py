import tkinter as tk


def vykresli_obrazok(subor, invert=False):
    canvas.delete("all")
    with open(subor, 'r') as f:
        sirka, vyska = map(int, f.readline().split())
        y = 0
        for riadok in f:
            hodnoty = riadok.strip().split()
            if not hodnoty:
                continue
            x = 0
            farba = 'black' if not invert else 'white'
            for cislo in hodnoty:
                pocet = int(cislo)
                for i in range(pocet):
                    # vykreslíme 1×1 pixel
                    canvas.create_rectangle(x, y, x+1, y+1, fill=farba, outline='')
                    x += 1
                # po každom úseku farbu prehodíme
                farba = 'white' if farba == 'black' else 'black'
            y += 1



def zmena_farieb():
    global invertovane
    invertovane = not invertovane
    vykresli_obrazok('zadanie_19.txt', invert=invertovane)



root = tk.Tk()
root.title("Zadanie 19 – Komprimovaný obrázok")


with open('zadanie_19.txt', 'r') as f:
    sirka, vyska = map(int, f.readline().split())

canvas = tk.Canvas(root, width=sirka, height=vyska, bg='white')
canvas.pack()


invertovane = False


vykresli_obrazok('zadanie_19.txt')


button = tk.Button(root, text="Zmeniť farby", command=zmena_farieb)
button.pack(pady=10)

root.mainloop()

