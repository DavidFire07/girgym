import re
kody_jedal = {'z':0,
              'c':0,
              'm':0,
              'o':0}
counter = 0
regex = '[0-9]+.([a-z])'
with open('zadanie_20.txt','r') as f:
    for line in f.readlines():
        counter += 1
        kod_jedla = re.search(regex,line)
        kody_jedal[kod_jedla.group(1)] += 1


print(f'Celkovy pocet objednanych jedal: {counter}')
print(kody_jedal)
for k,v in kody_jedal.items():
    if v < 20:
        print(f'Kod jedla {k} si objednalo menej ako 20 stravnikov')
    else:
        print(f'Kod jedla {k} si objednalo {v} stravnikov')

