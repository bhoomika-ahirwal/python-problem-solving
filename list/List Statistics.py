numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

if not numbers:
    print("List cannot be empty")
else:
    total = sum(numbers)
    average = total / len(numbers)

    print("\nList Statistics")
    print("----------------")
    print("Numbers :", numbers)
    print("Sum     :", total)
    print("Average :", average)
    print("Minimum :", min(numbers))
    print("Maximum :", max(numbers))