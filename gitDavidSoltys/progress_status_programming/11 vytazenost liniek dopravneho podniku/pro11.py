file = open("bus_vytazenost.txt", "r", encoding="Windows-1250")
header = file.readline()
data = [line.strip().split() for line in file.readlines()]
file.close()

bus_stop_count = 0
bus_stops = []

passangers_current_count = 0
passangers_highest_count = 0
bus_stops_exceded_limit = []
bus_limit = 50

for i, line in enumerate(data):

    if len(line) != 3:
        data[i] = data[i][:-2] + [" ".join(data[i][-2:])] 

    if line[2] not in bus_stops:
            bus_stops.append(line[2])
            bus_stop_count += 1

    passangers_current_count += int(line[0])
    passangers_current_count -= int(line[1])

    if passangers_current_count > bus_limit:
         bus_stops_exceded_limit.append(line[2])

    if passangers_current_count > passangers_highest_count:
         passangers_highest_count = passangers_current_count


print(f"Count of bus stops: {bus_stop_count}", end="\n" * 2)

print("Bus stops: ")
for bus_stop in bus_stops:
    print(bus_stop)

print()

if bus_stops_exceded_limit:
    print("Bus stops where bus limit was exceded: ")
    
    for bus_stop in bus_stops_exceded_limit:
        print(bus_stop)

    print()    

if passangers_highest_count > bus_limit:
     print(f"Highest count of passangers was {passangers_highest_count}")



