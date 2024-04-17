"""
The marks obtained by a student in 3 different subjects are input by the user. Your program should calculate the average of subjects and display the grade. The student gets a grade as per the following rules:
Average Grade
90-100 A
80-89 B
70-79 C
60-69 D
0-59 F

"""

# Accept marks for three subjects from the user

subject1 = int(input("Enter marks for subject 1: "))
subject2 = int(input("Enter marks for subject 2: "))
subject3 = int(input("Enter marks for subject 3: "))

# Calculate average marks
average_marks = (subject1 + subject2 + subject3) / 3

# grade based on average marks
if average_marks >= 90:
    grade = "A"
elif average_marks >= 80:
    grade = "B"
elif average_marks >= 70:
    grade = "C"
elif average_marks >= 60:
    grade = "D"
else:
    grade = "F"

# Display the grade
print("The average grade for the student is:", grade)
