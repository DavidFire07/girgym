x = []
pocet_ludi = 0
zastavky_cez_limit = []
presah_cestujucich = []
with open('zadanie_11.txt','r') as f:
    max_cestujucich = f.readline()
    for line in f.readlines():
        casti = line.strip().split(' ')
        x.append(' '.join(casti[2:]))
        pocet_ludi += int(casti[0])
        pocet_ludi -= int(casti[1])
        if pocet_ludi > int(max_cestujucich):
            zastavky_cez_limit.append(' '.join(casti[2:]))
            presah_cestujucich.append(pocet_ludi)




print(f'Pocet zastavok: {len(x)}')
print(f'Zastavky: {', '.join(x)}')
print(f'Zastavky cez limit: {', '.join(zastavky_cez_limit)}')
print(f'Najviac cestujucich cez limit bolo: {max(presah_cestujucich) - 50}')