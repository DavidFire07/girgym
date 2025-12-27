def decomprese_line(compresed_line):
    counter = 0
    decompresed_line = ""

    for i, num in enumerate(compresed_line):
        if i % 2 == 0:
            decompresed_line += "0" * int(num)
        else:
            decompresed_line += "1" * int(num)
    return decompresed_line


input_file = open("dekompresia_obrazka_1.txt", "r") 

header = input_file.readline().strip().split()
lines = input_file.readlines()

print(f"width of image is {header[0]}")
print(f"height of image is {header[1]}")

output_file = open("output_file.txt", "w")
for line in lines:
    line = line.strip().split()
    output_file.write(decomprese_line(line) + "\n")

input_file.close()
output_file.close()