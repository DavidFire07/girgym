pocet_cestujucich = 0
odporucania = []
automat_na_listky = []
zastavky_na_znamenie = []
with open("zadanie_3.txt","r") as f:
    for riadok in f:
        casti = riadok.strip().split(";")
        pocet_cestujucich += int(casti[0])
        pocet_cestujucich -= int(casti[1])
        odporucania.append(pocet_cestujucich)
        print(f"{casti[2]} ma {pocet_cestujucich} cestujucich")
        if pocet_cestujucich >= 10:
            automat_na_listky.append(casti[2])
        if int(casti[0]) < 3 or int(casti[1]):
            zastavky_na_znamenie.append(casti[2])


najvyssi_pocet_cestujucich = max(odporucania)

if najvyssi_pocet_cestujucich <= 33:
    print("Mala elektricka")
elif najvyssi_pocet_cestujucich <= 66:
    print("Stredna elektricka")
else:
    print("Dlha elektricka")

print("Zastavky kde je vhodne umiestnit automat:")
for zastavka in automat_na_listky:
    print(zastavka, end=", ")

print()
print("Zastavky na znamenie:")
for zastavka in zastavky_na_znamenie:
    print(zastavka, end=", ")



