sifry = [['0',' '], ['1', 'A', 'B', 'C'], ['2','D','E','F'],['3','G','H','I'],['4', 'J','K','L'],['5','M','N','O'],['6','P','Q','R'],['7','S','T','U'],['8','V','W','X'],['9','Y','Z']]
pocetnost = {'0': 0,
             '1': 0,
             '2': 0,
             '3': 0,
             '4': 0,
             '5': 0,
             '6': 0,
             '7': 0,
             '8': 0,
             '9': 0}

pismena = input('Prosim zadajte svoje vyraz').upper()
x = []
for pismeno in pismena:
    for sifra in sifry:
        if pismeno in sifra:
            cislo = sifra.index(pismeno)
            x.append(sifra[0] * (cislo))
            pocetnost[sifra[0]] += 1


print(' '.join(x))
max_pocetnost = [k for k,v in pocetnost.items() if v == max(pocetnost.values())]
print(f'Najcastejsie pouzivana tabulka: {max_pocetnost}')
