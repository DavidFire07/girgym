vstup = input('Prosim zadajte vetu, ktora bude obsahovat len znaky anglickej abecedy:')
#Cez vikend je planovana odstavka severnej casti linky

zoznam = vstup.split()
slova_na_kompresiu = []
for index,slovo in enumerate(zoznam):
    if index % 2 == 0:
        slova_na_kompresiu.append(slovo.upper())
    else:
        slova_na_kompresiu.append(slovo.lower())
print(f'Oznam pozostava z {len(zoznam)} slov')
print(''.join(slova_na_kompresiu))


dekomprimovane_slova = []
for slovo in slova_na_kompresiu:
    dekomprimovane_slova.append(slovo.upper())
print(' '.join(dekomprimovane_slova))
