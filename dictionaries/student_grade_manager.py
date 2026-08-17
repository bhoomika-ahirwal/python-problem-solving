students = {}

count = int(input("Enter number of students: "))

for i in range(count):
    name = input(f"\nEnter student {i + 1} name: ")
    marks = float(input("Enter marks: "))

    students[name] = marks

print("\nStudent Grade Report")
print("--------------------")

for name, marks in students.items():

    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B+"
    elif marks >= 60:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "F"

    print(f"{name}: {marks} - Grade {grade}")