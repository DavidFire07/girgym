import random

pocet_studentov = int(input('Prosim zadajte pocet studentov: '))
pocet_otazok = int(input('Prosim zadajte pocet otazok: '))

if pocet_otazok < pocet_studentov:
    raise Exception('Pocet otazok musi byt vacsi ako studentov')

parne = list(range(2,pocet_otazok + 1,2))
neparne = list(range(1,pocet_otazok,2))

random.shuffle(parne)
random.shuffle(neparne)

studenti = random.sample(range(1,pocet_studentov+1),pocet_studentov)

for i, student in enumerate(studenti):
    if i % 2 == 0:
        if parne:
            otazka = parne.pop(0)
        else:
            otazka = neparne.pop(0)
    else:
        if neparne:
            otazka = neparne.pop(0)
        else:
            otazka = parne.pop(0)

    print(f"Študent {student} má otázku {otazka}")