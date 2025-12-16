import re
upraveny_riadok = []
output = []

def spracuj_riadok(riadok):
    counter_0 = 0
    counter_1 = 0
    counter = 0
    if riadok[0] != '0':
        upraveny_riadok.append('0')
    for cislo in riadok:
        if cislo == '1':
            if counter_0 != 0:
                upraveny_riadok.append(str(counter_0))
                counter_0 = 0
            counter_1 += 1
        elif cislo == '0':
            if counter_1 != 0:
                upraveny_riadok.append(str(counter_1))
                counter_1 = 0
            counter_0 += 1

    if counter_0 != 0:
        upraveny_riadok.append(str(counter_0))
    elif counter_1 != 0:
        upraveny_riadok.append(str(counter_1))

with open('zadanie_14.txt','r') as f:
    x = f.readline()
    for line in f.readlines():
        spracuj_riadok(line.strip())
        output.append(' '.join(upraveny_riadok))
        print(' '.join(upraveny_riadok))
        upraveny_riadok.clear()

with open('zadanie_14_output.txt','a') as f:
    f.write(x)
    for line in output:
        f.write(f"{line}\n")

regex = '([0-9]+).([0-9]+)'
sirka_vyska = re.search(regex, x)
print(f'Sirka obrazka: {sirka_vyska.group(1)}, Vyska obrazka: {sirka_vyska.group(2)}, Pocet vsetkych bodov: {int(sirka_vyska.group(1)) * int(sirka_vyska.group(2))}')
