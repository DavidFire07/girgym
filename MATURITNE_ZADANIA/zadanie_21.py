subor = 'zadanie_21_output.txt'
def spracuj_riadok(riadok):
    counter = 0
    retaz = []
    line = riadok.strip().split()
    for index,cislo in enumerate(line):
        counter += 1
        if int(cislo) != 0 and index == 0:
            retaz.append((int(cislo) * '0'))
        if int(cislo) > 0 and index != 0:
            if counter % 2 == 1:
                retaz.append((int(cislo) * '0'))
            elif counter % 2 == 0:
                retaz.append((int(cislo) * '1'))
    return ''.join(retaz)

with open('zadanie_21.txt','r') as f:
    sirka, vyska = f.readline().split()
    for riadok in f.readlines():
        with open(subor,'a') as file:
            file.write(spracuj_riadok(riadok) + "\n")


print(f'Sirka {sirka}, Vyska {vyska}')