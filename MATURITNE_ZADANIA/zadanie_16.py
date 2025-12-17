frekvencia = {
    'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
    'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
    'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
}

with open('zadanie_16.txt','r') as f:
    for line in f.readlines():
        riadok = line.strip().split()
        print(' '.join(riadok))

with open('zadanie_16.txt', 'r') as f:
    for line in f.readlines():
        riadok = line.strip().split()
        for slovo in riadok:
            for pismeno in slovo:
                if pismeno not in "0123456789.,():;'-":
                    frekvencia[pismeno.lower()] += 1
ziadne_pismena = []
for k,v in frekvencia.items():
    print(f'{k} - {v}')
    if v == 0:
        ziadne_pismena.append(k)

print(f'V texte sa nevyskitli znaky: {' '.join(ziadne_pismena)}')
