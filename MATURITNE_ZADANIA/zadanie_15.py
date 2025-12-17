import random
import re

priklady = []
priklady_bez_vysledov = []
vysledky = []
pocet_bodov = 0
zle_vypocitane_priklady = []

for i in range(10):
    number_1 = random.randint(0, 10)
    number_2 = random.randint(0, 10)
    vysledok = number_1 * number_2
    priklady.append(f"{number_1} * {number_2} = {vysledok}")
    priklady_bez_vysledov.append(f"{number_1} * {number_2 } =")
    vysledky.append(vysledok)

for index,priklad in enumerate(priklady_bez_vysledov):
    user_input = input(priklad)
    if int(user_input) == vysledky[index]:
        pocet_bodov += 1
    else:
        zle_vypocitane_priklady.append(priklad)



regex = '([0-9])+...([0-9])'

index = 0
while zle_vypocitane_priklady:
    user_input = input(zle_vypocitane_priklady[index])
    cislo = re.search(regex, zle_vypocitane_priklady[index])
    if int(user_input) == int(cislo.group(1)) * int(cislo.group(2)):
        zle_vypocitane_priklady.remove(zle_vypocitane_priklady[index])

print(f'Pocet bodov: {pocet_bodov}')

with open('zadanie_15.txt','a') as f:
    for priklad in priklady:
        f.write(f'{priklad}\n')
