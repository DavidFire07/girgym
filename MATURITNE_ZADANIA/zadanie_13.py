import random
prehodene_slova = []

def randomiser(text):
    for slova in text:
        slovo = slova[1:-1]
        cast_slovo = random.sample(slovo,len(slovo))
        if len(slova) == 1:
            prehodene_slova.append(slova)
        else:
            prehodene_slovo = slova[0] + ''.join(cast_slovo) + slova[-1]
            prehodene_slova.append(prehodene_slovo)
    return prehodene_slova


with open('zadanie_13.txt','r') as f:
    for line in f:
        casti = line.strip().split()
        print(' '.join(casti))
print('-------------------------------------------------------------------')
with open('zadanie_13.txt', 'r') as f:
    for line in f:
        casti = line.strip().split()
        print(' '.join(randomiser(casti)))
        prehodene_slova.clear()