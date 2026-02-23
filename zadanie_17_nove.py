import random

riadky = []

with open('zadanie_17_nove.txt','r') as f:
    for line in f.readlines():
        slovicko = line.strip()
        riadky.append(slovicko)

slova = []

for i in range(0, len(riadky), 2):
    slovenske = riadky[i]
    anglicke = riadky[i + 1]
    slova.append((slovenske, anglicke))

random.shuffle(slova)

pocet_bodov = 0
nespravne_odpovede = []
smer = input('Preklad do: sk/en: ')

for dvojica in slova:
    sk, en = dvojica
    if smer.lower() == 'en':
        otazka = input(f'{sk}: ')
        if otazka.lower() == en:
            pocet_bodov += 1
        else:
            nespravne_odpovede.append(dvojica)
    if smer.lower() == 'sk':
        otazka = input(f'{en}: ')
        if otazka.lower() == sk:
            pocet_bodov += 1
        else:
            nespravne_odpovede.append(dvojica)

print(nespravne_odpovede)

while nespravne_odpovede:
    for dvojica in nespravne_odpovede:
        sk, en = dvojica
        if smer.lower() == 'en':
            otazka = input(f'{sk}: ')
            if otazka.lower() == en:
                nespravne_odpovede.pop(0)
        if smer.lower() == 'sk':
            otazka = input(f'{en}: ')
            if otazka.lower() == sk:
                nespravne_odpovede.pop(0)


print(f'Percentualna uspesnost: {pocet_bodov / 20 * 100}')
print(f'Pocet nespravnych odpovedi: {20 - pocet_bodov}')

with open('chyby.txt','w') as f:
    for i in nespravne_odpovede:
        f.write(f'{i}\n')