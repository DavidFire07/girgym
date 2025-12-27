import random as r

math_problmes = [[r.randint(1, 10), r.randint(1, 10)] for i in range(10)]
score = 0
first_try = True

file = open("nasobylka_vystup.txt", "w")
file.writelines(f"{math_problem[0]} * {math_problem[1]} =\n" for math_problem in math_problmes)
file.close()

while math_problmes:
    
    for math_problme in math_problmes[:]:
        answer = input(f"{math_problme[0]} * {math_problme[1]} = ")
        
        if int(answer) == (math_problme[0] * math_problme[1]):
            math_problmes.remove(math_problme)
            
            if first_try:
                score += 1
        
        print(score)
    
    first_try = False

print(f"Your final score is {score}/10")
