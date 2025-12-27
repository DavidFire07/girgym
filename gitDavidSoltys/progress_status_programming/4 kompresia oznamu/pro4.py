data = input()

words = data.strip().split(" ")

print(f"Zoznam je dlhy: {len(words)} slov")
compressed_message = ""

big = True

for word in words:
    if big:
        compressed_message += word.upper()
        big = False
    else:
        compressed_message += word.lower()
        big = True
    
print(f"Stlacena sprava: {compressed_message}")
print(f"{compressed_message.upper()}")