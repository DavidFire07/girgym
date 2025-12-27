import string as s

with open("tabulka_pocetnosti.txt", "r") as file:
    
    table = {char: 0 for char in s.ascii_uppercase}

    for line in file:
        line = line.strip()
        print(line)
        
        for char in line:
            char = char.upper()

            if char.isalpha():
                table[char.upper()] += 1

print()
print("Chars that have occured in the text: ")
for key, value in table.items():
    if value != 0:
        print(f"{key} - {value}")

print()
print("Chars that haven't occured in the text: ")
for key, value in table.items():
    if value == 0:
        print(f"{key} - {value}")