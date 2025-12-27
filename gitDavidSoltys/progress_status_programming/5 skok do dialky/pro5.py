with open('skok_do_dialky.txt', 'r') as file:
    data = file.readlines()

for i, line in enumerate(data):
    data[i] = line.strip().split(' ')

countries = set()
for line in data:
    country = line[1]
    countries.add(country)

print('Krajiny: ', end='')
for country in countries:
    print(country, end='  ')

parcipitants_num = {}
for line in data:
    country = line[1]
    parcipitants_num[country] = parcipitants_num.get(country, 0) + 1

print()
print('Počet účastníkov určitej krajiny: ', end='')
for country in parcipitants_num:
    print(country + ': ' + str(parcipitants_num[country]), end='  ')

for i, line in enumerate(data):
    scores = line[-5:]
    best_score = max(map(int, scores))
    data[i] = line[:2] + [best_score]

best_jumpers = []
best_score = max(line[-1] for line in data)

for line in data:
    if line[-1] == best_score:
        best_jumpers.append(line[0])

print()
if len(best_jumpers) == 1:
    print(f'Najlepší skokan je: {best_jumpers[0]}')
else:
    print('Najlepší skokani sú: ', end='')
    for jumper in best_jumpers:
        print(jumper, end=' ')

