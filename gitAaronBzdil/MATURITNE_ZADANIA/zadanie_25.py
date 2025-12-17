pocet_sportovcov = 0
data = []
with open('zadanie_25.txt','r') as f:
    for line in f.readlines():
        pocet_sportovcov += 1
        v = line.strip().split()
        data.append(v)

dict_of_sportovci = {item[0]: int(item[1]) for item in data}

data = []
for k,v in dict_of_sportovci.items():
    print(f'Sutaziaci {k} dobehol do ciela za {v} sekund')
    data.append(v)
print('--------------------------------------')

najmensia_hodnota = min(data)
minuty = najmensia_hodnota // 60
sekundy = najmensia_hodnota % 60

for k,v in dict_of_sportovci.items():
    if v == najmensia_hodnota:
        print(f'Najlepsi sutaziaci - {k} s casom: {minuty} min : {sekundy} sek')
print('--------------------------------------')
print(f'Pocet zucastnenych sportovcov: {pocet_sportovcov}')
