pocet_merani = 0
namerane_teploty_str = []
stanice = []
namerane_teploty_float= []
with open('zadanie_28.txt','r') as f:
    for line in f.readlines():
        pocet_merani += 1
        riadok = line.strip().split()
        namerane_teploty_str.append(riadok[3])
        stanice.append(riadok[0])


print(f'Pocet vsetkych merani: {pocet_merani}')
for teplota in namerane_teploty_str:
    print(teplota)
    if teplota[0] == '-':
        namerane_teploty_float.append(float('-'+teplota[1:3]+'.'+teplota[4:]))
    elif teplota[0] == '+':
        namerane_teploty_float.append(float(teplota[1:3]+'.'+teplota[4:]))

najvacsia_teplota = max(namerane_teploty_float)
index_stanice = namerane_teploty_float.index(najvacsia_teplota)
print(f'Najvacsia teplota {najvacsia_teplota} bola namerana na stanici: {stanice[index_stanice]}')

priemerna_teplota = sum(namerane_teploty_float) / len(namerane_teploty_float)
print(f'Priemerna teplota na staniciach: {priemerna_teplota}')


