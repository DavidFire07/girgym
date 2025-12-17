import re

regex = r'([0-9]+):([0-9]+)\s*(.+)'
pocet_vyjadreni = 0
hodiny_dna = []
pocet_dni = 1
reakcia_na_den = 0
pocet_reakci_dni = []

predosla_hodina = -1
predosla_minuta = -1

with open('zadanie_22.txt', 'r', encoding='latin-1') as f:
    for index, line in enumerate(f.readlines()):
        line = line.strip()
        if not line:
            continue

        vyraz = re.search(regex, line)
        if not vyraz:
            continue

        hodina = int(vyraz.group(1))
        minuta = int(vyraz.group(2))


        pocet_vyjadreni += 1
        hodiny_dna.append(hodina)
        reakcia_na_den += 1


        if predosla_hodina != -1 and (hodina < predosla_hodina or (hodina == predosla_hodina and minuta < predosla_minuta)):
            pocet_dni += 1
            pocet_reakci_dni.append(reakcia_na_den - 1)
            reakcia_na_den = 1

        predosla_hodina = hodina
        predosla_minuta = minuta

pocet_reakci_dni.append(reakcia_na_den)


for index, den in enumerate(pocet_reakci_dni):
    print(f"{index + 1}. deň - počet reakcií: {den}")

print(f"Počet všetkých vyjadrení: {pocet_vyjadreni}")


hodiny_skontrolovane = []
for h in hodiny_dna:
    if h not in hodiny_skontrolovane:
        print(f"Hodina:{h} Reakcií zákazníkov:{hodiny_dna.count(h)}")
        hodiny_skontrolovane.append(h)

print(f"Počet dní: {pocet_dni}")
