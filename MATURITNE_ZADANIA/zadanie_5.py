country = set()
participants = dict()
winner = dict()

content = open("zadanie_5.txt", "r")
for line in content:
    parts = line.strip().split()
    country.add(parts[1])
    number = 1
    if parts[1] not in participants:
        participants.update({parts[1] : 1})
    elif parts[1] in participants:
        number += 1
        participants.update({parts[1] : number})
    name = parts[0]
    score = max(parts[2:])
    winner.update({name : score})

def win():
    p = max(winner.values())
    for i in winner.items():
        if i[1] == p:
            print(f"Vitazom je: {i}")
def coun():
    print(f"Sutaziace krajiny: {country}")
def part():
    print(f"Pocet sutaziacich z roznych krajin: {participants}")

coun()
part()
win()