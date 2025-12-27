with open("ucenie_sa_slovicok.txt", "r") as file:
    
    sk = []
    en = []
    i = 0

    for word in file:
        word = word.strip()

        if i % 2 == 0:
            sk.append(word)
        else:
            en.append(word)
        i += 1
    
    answer = input("If you want to be given slovak words (S), if you want to be given english words (E): ")
    
    if answer == "S":
        main = sk
        sub = en
    elif answer == "E":
        main = en
        sub = sk

    incorrect_attemps = 0
    while main[:]:
        for word in main:
            i = main.index(word)
            translation = input(f"Translate {word}: ")

            if sub[i] == translation:
                del main[i]
                del sub[i]
            else:
                incorrect_attemps += 1

    print(f"You have made {incorrect_attemps} mistakes.")