pocet_sms = 0
subor = 'zadanie_24_'
pripona = '.txt'

#
zoznamy = {str(5220 + i): [] for i in range(10)}

with open('zadanie_24.txt', 'r', encoding='utf-8') as f:
    for line in f:
        kod = line.strip()
        if not kod:
            continue
        pocet_sms += 1
        if kod in zoznamy:
            zoznamy[kod].append(pocet_sms)


for kod, data in zoznamy.items():
    with open(f'{subor}{kod}{pripona}', 'a', encoding='utf-8') as f:
        for cislo in data:
            f.write(f'{cislo}\n')

print(f'Počet všetkých zaslaných SMS: {pocet_sms}')
