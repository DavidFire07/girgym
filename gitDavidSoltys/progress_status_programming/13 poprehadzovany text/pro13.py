import random as r

input_file = open("poprehadzovany_text1_vstup.txt", "r")
data = [line.strip() for line in input_file.readlines()]

text = []
for line in data:
    text += line.split(" ")

for i, word in enumerate(text):
    if len(word) > 2:
        middle = list(word[1:-1])
        r.shuffle(middle)
        text[i] = str(word[0] + str("".join(middle)) + word[-1])

text = " ".join(text)
print(text)

outpu_file = open("shuffeld_text.txt", "w", encoding="UTF-8")
outpu_file.write(text)

input_file.close()
outpu_file.close()