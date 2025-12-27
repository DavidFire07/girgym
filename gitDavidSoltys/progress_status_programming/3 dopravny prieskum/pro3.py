with open('dopravny_prieskum.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()

passengers_count = 0
passengers_counts = []
ticket_machines = []
sign_stations = []

for line in lines:
    line = line.strip().split(';')
    passengers_count += int(line[0]) - int(line[1])
    passengers_counts.append(passengers_count)
    print(f"{line[2]} {passengers_count}")
    if int(line[0]) >= 10:
        ticket_machines.append(line[2])
    if int(line[1]) < 3 or int(line[1]) < 3:
        sign_stations.append(line[2])


passengers_highest_count = max(passengers_counts)

if passengers_highest_count <= 33:
    print("Typ elektricky: kratka")
elif passengers_highest_count <= 66:
    print("Typ elektricky: standarna")
else:
    print("Typ elektricky: dlha")

print("Zastavky kde je vhodne umiestnit automat: ")
for station in ticket_machines:
    print(station, end=", ")

print("\n")
print("Zastavky na znamenie: ")
for station in sign_stations:
    print(station, end=", ")

