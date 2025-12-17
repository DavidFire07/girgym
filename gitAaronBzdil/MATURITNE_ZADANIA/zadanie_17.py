riadok = 2
svk_slova = []
eng_slova = []
with open('zadanie_17.txt','r') as f:
    for line in f.readlines():
        if riadok % 2 == 0:
            riadok += 1
            svk_slova.append(line.strip())
        elif riadok % 2 == 1:
            riadok += 1
            eng_slova.append(line.strip())

moznost = input('Prosim vyberte ci chcete hadat slovensky alebo anglicky preklad:')
zle_odpovede = 0
znovu_vyskusat = []
preklad = []

if moznost.lower() == 'slovensky':
    for index,slovo in enumerate(svk_slova):
        vstup = input(f'{slovo}: ')
        if vstup == eng_slova[index]:
            pass
        else:
            zle_odpovede += 1
            znovu_vyskusat.append(slovo)
            preklad.append(eng_slova[index])
    while znovu_vyskusat:
        vstup = input(f'{znovu_vyskusat[0]}: ')
        if vstup == preklad[0]:
            znovu_vyskusat.pop(0)
            preklad.pop(0)
        else:
            zle_odpovede += 1
elif moznost.lower() == 'anglicky':
    for index,slovo in enumerate(eng_slova):
        vstup = input(f'{slovo}: ')
        if vstup == svk_slova[index]:
            pass
        else:
            zle_odpovede += 1
            znovu_vyskusat.append(slovo)
            preklad.append(svk_slova[index])
    while znovu_vyskusat:
        vstup = input(f'{znovu_vyskusat[0]}: ')
        if vstup == preklad[0]:
            znovu_vyskusat.pop(0)
            preklad.pop(0)
        else:
            zle_odpovede += 1
else:
    print('Vami zadani prikaz je nezrozumitelny...')

print(f'Pocet zlych odpovedi: {zle_odpovede}')