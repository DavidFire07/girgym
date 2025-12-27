import random as r

students_count = int(input("Enter number of students: "))
questions_count = int(input("Enter number of students: "))

while students_count > questions_count:
    students_count = int(input("Enter number of students: "))
    questions_count = int(input("Enter number of students: "))

students = [i + 1 for i in range(students_count)]
questions = [i + 1 for i in range(questions_count)]

r.shuffle(students)
r.shuffle(questions)

"""
questions = []
odd_questions = [i + 1 for i in range(questions_count) if (i + 1) % 2 == 1]
even_questions = [i + 1 for i in range(questions_count) if (i + 1) % 2 == 0]

r.shuffle(odd_questions)
r.shuffle(even_questions)

if questions_count % 2 == 0:
    for i in range(int(questions_count / 2)):
        questions.append(odd_questions[i])
        questions.append(even_questions[i])
else:
    for i in range(int((questions_count - 1) / 2)):
        questions.append(odd_questions[i])
        questions.append(even_questions[i])
    questions.append[odd_questions[questions_count / 2 + 1]]
    
"""

for i in range(len(students)):
    print(f"{i + 1}. student: {students[i]}; question: {questions[i]}")