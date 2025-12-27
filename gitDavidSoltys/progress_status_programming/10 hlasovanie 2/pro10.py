file1 = open("hlasovanie_2.txt", "r")
messages = [line.strip() for line in file1.readlines()]
file1.close()

file2 = open("hlasovanie_vypadnuti.txt", "r")
excluded = [line.strip() for line in file2.readlines()]
file2.close()

messanges_total_count = len(messages)
print(f"Total nubmer of messanges is {messanges_total_count}")
print()

messanges_count = {}
for message in messages:
    messanges_count[message] = messanges_count.get(message, 0) + 1

print("Displaying votes of all candidates: ")
for key, value in messanges_count.items():
    print(f"{key}: {value}")
print()

print("Displaying votes of candidates who weren't excluded: ")
for key, value in messanges_count.items():
    if key not in excluded:
        print(f"{key}: {value}")

