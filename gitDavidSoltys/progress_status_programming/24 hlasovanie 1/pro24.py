with open("hlasovanie_1.txt", "r") as file:
    data = [vote.strip() for vote in file.readlines()]

headers = []
table = []

for i, vote in enumerate(data):

    if vote not in headers:
        headers.append(vote)
        table.append([])

    table[headers.index(vote)].append(str(i + 1))

for header in headers:
    with open(header + ".txt", "w") as file:
        votes = table[headers.index(header)]
        file.writelines(vote + "\n" for vote in votes)