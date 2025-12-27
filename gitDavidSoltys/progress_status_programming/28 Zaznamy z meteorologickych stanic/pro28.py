with open("meteo_stanice.txt", "r") as file:
    data = [line.strip().split() for line in file.readlines()]

print(f"Number of measurements: {len(data)}")
print()

for measurement in data:
    print(f"Temperature: {measurement[3]}")
print()

station_code, heighest_temperature = max(((measurement[0], float(measurement[3].replace(",", "."))) for measurement in data), key=lambda x: x[1])
print(f"The heighest measured temeprature: {heighest_temperature} at station: {station_code}")
print()

average_temperature = round(sum(float(measurement[3].replace(",", ".")) for measurement in data) / len(data), 3)
print(f"Average temperature of all stations is {average_temperature}")
print()