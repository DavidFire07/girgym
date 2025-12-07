import csv
import tkinter as tk
from tkinter import ttk

def log_error(row, error):
    with open("errors.log", "a", encoding="utf-8") as file:
        file.write(f"{error} | {row}\n")
    return 0

studet_quantity = 0
best_student = None
best_results_subject = None
top_3_students = []
student_avg_mark = {}
subject_avg_mark = {"math": 0,
                     "slovak_language": 0,
                     "english_language": 0,}
students_info = {}

with open("ziaci.csv", "r", encoding="utf-8") as file:
    data = csv.DictReader(file)

    for row in data:

        first_name = row.get("meno")
        second_name = row.get("priezvisko")
        grade = row.get("rocnik")
        math = row.get("matematika")
        slovak_language = row.get("slovencina")
        english_language = row.get("anglictina")
        attendance = row.get("dochadzka")

        if not all([first_name, second_name, grade, math, slovak_language, english_language, attendance]):
            log_error(row, "missing field/s")
            continue

        try:
            first_name = str(first_name)
            second_name =str(second_name)
            grade = int(grade)
            math = int(math)
            slovak_language = int(slovak_language)
            english_language = int(english_language)
            attendance = int(attendance)
        except (ValueError, TypeError) as error:
            log_error(row, error)
            continue

        if ((not 1 <= grade <= 5) or
            (not 1 <= math <= 5) or
            (not 1 <= slovak_language <= 5) or
            (not 1 <= english_language <= 5)):
            
            log_error(row, "grade or mark out of range")
            continue

        if not 0 < attendance < 100:
            log_error(row, "attendance is out of range")
            continue
        
        studet_quantity += 1

        avg_mark = sum([math, slovak_language, english_language]) / 3
        student_avg_mark[(first_name, second_name)] = avg_mark
        
        subject_avg_mark["math"] += math
        subject_avg_mark["english_language"] += english_language
        subject_avg_mark["slovak_language"] += slovak_language

        students_info[f"{first_name} {second_name}"] = {"grade": grade, 
                                                        "english_language": english_language, 
                                                        "slovak_language": slovak_language,
                                                        "math": math, 
                                                        "attendance": attendance,
                                                        "avg_mark": avg_mark}

subject_avg_mark["math"] = subject_avg_mark["math"] / studet_quantity
subject_avg_mark["english_language"] = subject_avg_mark["english_language"] / studet_quantity
subject_avg_mark["slovak_language"] = subject_avg_mark["slovak_language"] / studet_quantity

best_results_subject = min(subject_avg_mark.items(), key=lambda x: x[1])

top_3_students = sorted(student_avg_mark.items(), key=lambda x: x[1], reverse=True)[0:4]

best_student = top_3_students[0]

with open("vysledok.txt", "w", encoding="utf-8") as file:
    
    file.write("Students' average marks:\n")
    for student, avg_mark in student_avg_mark.items():
        file.write(f"{student[0]} {student[1]} {avg_mark:.2f}\n")

    file.write("\nSubjects' average marks:\n")
    for subject, avg_mark in subject_avg_mark.items():
        file.write(f"{subject} {avg_mark:.2f}\n")

    file.write("\nTop 3 students are:\n")
    for student in top_3_students:
        file.write(f"{student[0][0]} {student[0][1]}\n")

students = [student for student in students_info]
students = sorted(students)

def press_button():
    name = dropdown_menu.get()

    grade_info = str(students_info[name]["grade"])
    english_langueage_info = str(students_info[name]["english_language"])
    slovak_language_info = str(students_info[name]["slovak_language"])
    math_info = str(students_info[name]["math"])
    avg_mark_info = f"{students_info[name]["avg_mark"]:.2f}"
    attendance_info = str(students_info[name]["attendance"]) + "%"

    if grade_info == "1":
        grade_info += "st"
    elif grade_info == "2":
        grade_info += "nd"
    elif grade_info == "3":
        grade_info += "rd"
    else:
        grade_info += "th"

    label_grade_info.config(text=grade_info)
    label_english_language_info.config(text=english_langueage_info)
    label_slovak_language_info.config(text=slovak_language_info)
    label_math_info.config(text=math_info)
    label_average_mark_info.config(text=avg_mark_info)
    label_attendance_info.config(text=attendance_info)

# syle parameters
bg_color = "#1E1E1E"
fg_color ="white"
field_color = "#1E1E1E"
padding_all = (30, 12)

root = tk.Tk()
root.title("Student status")

style = ttk.Style()
style.theme_use("clam")   # Required, default themes often ignore colors

# styles
style.configure(
    "dark.TFrame",
    fieldbackground=field_color,
    background=bg_color,
    foreground=fg_color,
    font=("Arial", 22),
    padding=padding_all,
    borderwidth=1,
    relief="solid"
)

style.configure(
    "dark.TCombobox",
    fieldbackground=field_color,
    background=bg_color,
    foreground=fg_color,
    font=("Arial", 22),
    padding=padding_all,
    borderwidth=1,
    relief="solid"
)

style.configure(
    "dark.TButton",
    fieldbackground=field_color,
    background=bg_color,
    foreground=fg_color,
    font=("Arial", 22),
    padding=padding_all,
    borderwidth=1,
    relief="solid"
)

style.configure(
    "dark.TLabel",
    fieldbackground=field_color,
    background=bg_color,
    foreground=fg_color,
    font=("Arial", 22),
    padding=padding_all,
    borderwidth=1,
    relief="solid"
)

# MAIN FRAMES
left_frame = ttk.Frame(root, style="dark.TFrame")
left_frame.pack(side="left", fill="both", expand=True)

right_frame = ttk.Frame(root, style="dark.TFrame")
right_frame.pack(side="left", fill="both", expand=True)

# LEFT SUBFRAMES
sub_1_left_frame = ttk.Frame(left_frame, style="dark.TFrame")
sub_1_left_frame.pack(side="top", fill="both", expand=True)

sub_2_left_frame = ttk.Frame(left_frame, style="dark.TFrame")
sub_2_left_frame.pack(side="top", fill="both", expand=True)

# RIGHT SUBFRAMES
sub_1_right_frame = ttk.Frame(right_frame, style="dark.TFrame")
sub_1_right_frame.pack(side="top", fill="both", expand=True)

sub_2_right_frame = ttk.Frame(right_frame, style="dark.TFrame")
sub_2_right_frame.pack(side="top", fill="both", expand=True)

sub_3_right_frame = ttk.Frame(right_frame, style="dark.TFrame")
sub_3_right_frame.pack(side="top", fill="both", expand=True)

# LEFT side widgets
dropdown_menu = ttk.Combobox(sub_1_left_frame, font=("Arial", 22), values=students, style="dark.TCombobox")
dropdown_menu.pack(side="top", fill="x", expand=True)

submit_button = ttk.Button(sub_1_left_frame, text="Submit", style="dark.TButton", command=press_button)
submit_button.pack(side="top", fill="x", expand=True)

table_frame = ttk.Frame(sub_2_left_frame, style="dark.TFrame")
table_frame.pack(side="top", fill="both", expand=True)

headline = ttk.Label(table_frame, text="The top 3 students:", anchor="w", style="dark.TLabel")
headline.pack(side="top", fill="x", expand=True)

student_1 = ttk.Label(table_frame, text=top_3_students[0][0], anchor="w", style="dark.TLabel")
student_1.pack(side="top", fill="x", expand=True)

student_2 = ttk.Label(table_frame, text=top_3_students[1][0], anchor="w", style="dark.TLabel")
student_2.pack(side="top", fill="x", expand=True)

student_3 = ttk.Label(table_frame, text=top_3_students[2][0], anchor="w", style="dark.TLabel")
student_3.pack(side="top", fill="x", expand=True)

# RIGHT side widgets: two-column layout in 2nd right subframe
sub2_right_col_labels = ttk.Frame(sub_2_right_frame, style="dark.TFrame")
sub2_right_col_labels.pack(side="left", fill="both", expand=True)

sub2_right_col_info = ttk.Frame(sub_2_right_frame, style="dark.TFrame")
sub2_right_col_info.pack(side="left", fill="both", expand=True)

# Column 1: field labels (Grade + Subjects + Attendance)
label_grade = ttk.Label(sub2_right_col_labels, anchor="w", text="Grade:", style="dark.TLabel")
label_grade.pack(side="top", fill="both", expand=True)

label_slovak_language = ttk.Label(sub2_right_col_labels, anchor="w", text="Slovak language:", style="dark.TLabel")
label_slovak_language.pack(side="top", fill="both", expand=True)

label_english_language = ttk.Label(sub2_right_col_labels, anchor="w", text="English language:", style="dark.TLabel")
label_english_language.pack(side="top", fill="both", expand=True)

label_math = ttk.Label(sub2_right_col_labels, anchor="w", text="Math:", style="dark.TLabel")
label_math.pack(side="top", fill="both", expand=True)

label_average_mark = ttk.Label(sub2_right_col_labels, anchor="w", text="Average mark:", style="dark.TLabel")
label_average_mark.pack(side="top", fill="both", expand=True)

label_attendance = ttk.Label(sub2_right_col_labels, anchor="w", text="Attendance:", style="dark.TLabel")
label_attendance.pack(side="top", fill="both", expand=True)

# Column 2: info labels
label_grade_info = ttk.Label(sub2_right_col_info, anchor="w", text="0", style="dark.TLabel")
label_grade_info.pack(side="top", fill="both", expand=True)

label_slovak_language_info = ttk.Label(sub2_right_col_info, anchor="w", text="0", style="dark.TLabel")
label_slovak_language_info.pack(side="top", fill="both", expand=True)

label_english_language_info = ttk.Label(sub2_right_col_info, anchor="w", text="0", style="dark.TLabel")
label_english_language_info.pack(side="top", fill="both", expand=True)

label_math_info = ttk.Label(sub2_right_col_info, anchor="w", text="0", style="dark.TLabel")
label_math_info.pack(side="top", fill="both", expand=True)

label_average_mark_info = ttk.Label(sub2_right_col_info, anchor="w", text="0.00", style="dark.TLabel")
label_average_mark_info.pack(side="top", fill="both", expand=True)

label_attendance_info = ttk.Label(sub2_right_col_info, anchor="w", text="0%", style="dark.TLabel")
label_attendance_info.pack(side="top", fill="both", expand=True)

root.mainloop()