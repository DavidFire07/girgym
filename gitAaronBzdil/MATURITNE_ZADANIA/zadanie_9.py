counter = 0
counter_1 = 0
mena = []
priezviska = []
with open('zadanie_9.txt','r') as f:
    for line in f.readlines():
        counter += 1
        casti = line.strip().split(' ')
        mena.append(casti[:])
        if counter == 4:
            break

with open('zadanie_9.txt','r') as f:
    for line in f.readlines():
        counter_1 += 1
        if counter_1 < 5:
            continue
        casti = line.strip().split(' ')
        priezviska.append(casti[:])



mena = [' '.join(meno) for meno in mena]
priezviska = [' '.join(priezvisko) for priezvisko in priezviska]

print(f'Pocet mien: {len(mena)}')

x = []
x.append(mena[3])
for meno in mena:
    if len(meno) > len(x[0]):
        x.clear()
        x.append(meno)
print(f'Najdlhsie meno: {''.join(x)}')

y = []
y.append(priezviska[3])
for i in priezviska:
    if len(i) > len(y[0]):
        y.clear()
        y.append(i)
print(f'Najdhsie priezvisko: {''.join(y)}')

