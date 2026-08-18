def calculate_total(expenses):
    return sum(expenses)


def calculate_average(expenses):
    return sum(expenses) / len(expenses)


def find_highest(expenses):
    return max(expenses)


def display_summary(expenses):
    total = calculate_total(expenses)
    average = calculate_average(expenses)
    highest = find_highest(expenses)

    print("\nExpense Summary")
    print("----------------")
    print("Expenses :", expenses)
    print("Total    :", total)
    print("Average  :", round(average, 2))
    print("Highest  :", highest)


expenses = []

count = int(input("How many expenses do you have? "))

for i in range(count):
    amount = float(input(f"Enter expense {i + 1}: "))
    expenses.append(amount)

if expenses:
    display_summary(expenses)
else:
    print("No expenses entered.")