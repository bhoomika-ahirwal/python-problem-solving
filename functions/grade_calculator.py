def calculate_total(marks):
    return sum(marks)


def calculate_average(marks):
    return sum(marks) / len(marks)


def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B+"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F"


def display_result(marks):
    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = calculate_grade(average)

    print("\nStudent Result")
    print("--------------")
    print("Marks   :", marks)
    print("Total   :", total)
    print("Average :", round(average, 2))
    print("Grade   :", grade)


marks = []

subjects = int(input("Enter number of subjects: "))

for i in range(subjects):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

display_result(marks)def calculate_total(marks):
    return sum(marks)


def calculate_average(marks):
    return sum(marks) / len(marks)


def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B+"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F"


def display_result(marks):
    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = calculate_grade(average)

    print("\nStudent Result")
    print("--------------")
    print("Marks   :", marks)
    print("Total   :", total)
    print("Average :", round(average, 2))
    print("Grade   :", grade)


marks = []

subjects = int(input("Enter number of subjects: "))

for i in range(subjects):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

display_result(marks)