file = open("spokojnost_0.txt", "r")
expressions = [line.strip().split() for line in file.readlines()]
total_count = len(expressions)

print(f"Total number of expressions: {total_count}")

hours_count = {}
for expression in expressions:
    hours_count[expression[0][:2]] = hours_count.get(expression[0][:2], 0) + 1

print()
for hour, count in hours_count.items():
    print(f"Hour: {hour}; expressions: {count}")

print()
print(f"Number of days: {total_count}")

print()
for i in range(total_count):
    print(f"Day: {i + 1}; expresssions: {i + 1}")

file.close()