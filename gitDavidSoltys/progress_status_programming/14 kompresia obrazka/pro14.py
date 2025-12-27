def do_line(line):
    compressed_line = ''
    
    counter = 0
    prev_digit = line[0]

    if line[0] == "1":
        compressed_line += "0 "

    for digit in line:
        if digit == prev_digit:
            counter += 1
        else:
            compressed_line += str(counter) + " "
            prev_digit = digit
            counter = 1

    compressed_line += str(counter) + " "
    
    return compressed_line

with open("kompresia_obrazka.txt", "r") as input_f, open("skomprimovany_obrazok.txt", "w") as output_f:
    header = input_f.readline().strip().split()
    output_f.write(" ".join(header) + "\n")

    pixel_count = int(header[0]) * int(header[1])

    print(f"width: {header[0]} px")
    print(f"height: {header[1]} px")
    print(f"image size: {pixel_count} pixels")

    for line in input_f:
        compressed_line = do_line(line)
        output_f.write(compressed_line + "\n")