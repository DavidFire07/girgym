with open("mena_zamestnancov.txt", "r", encoding="utf-8") as file:
    data = file.read().split("\n")
    
    persons_counter = int(len(data) / 2)
    
    first_names = data[:persons_counter + 1]
    last_names = data[persons_counter:]
    
    longest_first_name_length = max([len(name) for name in first_names])
    longest_last_name_length = max([len(name) for name in last_names])
    boarder = longest_first_name_length + 3

    print(f"Number of names is {persons_counter}")
    print(f"Length of longest first name is {longest_first_name_length}")
    print(f"Length of ongest second name is {longest_last_name_length}")
    print()

    for i in range(persons_counter):
        print(first_names[i], end="")
        spaces = boarder - len(first_names[i])
        print(" " * spaces, end="")
        print(last_names[i])
    
