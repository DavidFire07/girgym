with open("sutaz_vbehu.txt", "r") as file:
    data = [line.strip().split() for line in file.readlines()]

print(f"Number of competitors: {len(data)}")
print()

for competitor in data:
    print(f"Competitor {competitor[0]} finished the race in {competitor[1]} seconds")
print()

best_time = min([time for competitor, time in data])
best_competitor = next(competitor for competitor, time in data if time == best_time)

minutes, seconds = divmod(int(best_time), 60)

print(f"Winner: {best_competitor} with time: {minutes}:{seconds:02d}")