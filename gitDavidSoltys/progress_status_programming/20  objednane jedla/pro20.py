with open("objednane_jedla.txt", "r") as file:
    data = [line.strip().split() for line in file.readlines()]

counter = {}
for line in data:
    counter[line[1]] = counter.get(line[1], 0) + 1

total_count = 0
for value in counter.values():
    total_count += value

print(f"Total number of dishes is {total_count}")

for key, value in counter.items():
    if value < 20:
        print(f"{key} - {value}  insuffient amount")
    else:
        print(f"{key} - {value}  suffient amount")