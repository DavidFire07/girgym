sutaziaci = {
    "5220": 0,
    "5221": 0,
    "5222": 0,
    "5223": 0,
    "5224": 0,
    "5225": 0,
    "5226": 0,
    "5227": 0,
    "5228": 0,
    "5229": 0}


pocet_riadkov = 0
with open('zadanie_10_sms.txt','r') as f:
    for line in f.readlines():
        pocet_riadkov += 1
        sutaziaci[line.strip()] += 1

print(f'Pocet vsetkych hlasov: {pocet_riadkov}')
for k,v in sutaziaci.items():
    print(f'Sutaziaci {k} mal {v} hlasov')
for k,v in sutaziaci.items():
    if v == min(sutaziaci.values()):
        print(f'Sutaziaci {k} mal najmenej hlasov a nepostupuje do dalsieho kola.')

x = []
with open('zadanie_10_vypadnuti.txt','r') as f:
    for line in f.readlines():
        riadok = line.strip()
        x.append(riadok)

sutaziaci.pop(x[0])
sutaziaci.pop(x[1])

for k,v in sutaziaci.items():
    if v == min(sutaziaci.values()):
        print(f'Sutaziaci {k} mal najmenej hlasov a nepostupuje do dalsieho kola.')