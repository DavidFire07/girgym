message = input("Enter your message: ")
encrypted_message = []

numbers_count = {}
for char in message:
    
    if char.isspace():
        print(0, end=" ")
        numbers_count[0] = numbers_count.get(0, 0) + 1
    
    elif char.isalpha():
        field = (ord(char) - ord("A")) // 3 + 1
        occurence = (ord(char) - ord("A")) % 3 + 1
        print(f"{str(field) * occurence}", end=" ") 
        numbers_count[field] = numbers_count.get(field, 0) + occurence

heighest_num = max(numbers_count.values())

print(f"Most frequently chosen fields: ", end="")
for key, value in numbers_count.items():
    if value == heighest_num:
        print(f"{key}", end=" ")

print()