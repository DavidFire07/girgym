user_input = input("Prosim vlozte text(Pouzite iba pismena a medzery):")

dlzka_vstupu = user_input.strip().split()
print(f"Pocet slov: {len(dlzka_vstupu)}")
kompressia_spravy = ""
velke = True
for slovo in dlzka_vstupu:
    if velke:
        kompressia_spravy += slovo.upper()
        velke = False
    else:
        kompressia_spravy += slovo.lower()
        velke = True

print(kompressia_spravy.upper())
