numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

unique_numbers = list(set(numbers))

if len(unique_numbers) < 2:
    print("At least two unique numbers are required")
else:
    unique_numbers.sort(reverse=True)
    print("Second largest number =", unique_numbers[1])