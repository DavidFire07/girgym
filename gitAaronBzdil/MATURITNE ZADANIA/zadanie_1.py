import random
hadane_slova = list()

with open("zadanie_1.txt","r") as f:
    for line in f:
        hadane_slova.append(line)

tajne_slovo = random.choice(hadane_slova)
dlzka_bodiek = (len(tajne_slovo) - 1) * "."


print(dlzka_bodiek)
index = 0

user_input = input("Uhadni pismeno tajneho slova:")
for i in range(10):
    if user_input == tajne_slovo[index]:
        bodky = (tajne_slovo[index] + "." * (len(dlzka_bodiek) - (index + 1)))
        name = (tajne_slovo[:index] + bodky)
        print(name)
        index += 1
        if (tajne_slovo[:index] + (tajne_slovo[index] + "." * (len(dlzka_bodiek) - (index + 1)))) == tajne_slovo:
            print("vyhral si")
            break
        user_input = input("Uhadni pismeno tajneho slova:")
    elif user_input != tajne_slovo[index]:
        print("zle pismeno")
        user_input = input("Pre pokracovanie klikni Enter")
        continue

