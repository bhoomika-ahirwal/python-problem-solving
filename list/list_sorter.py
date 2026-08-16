numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

choice = input("Sort ascending or descending? (a/d): ").lower()

if choice == "a":
    numbers.sort()
    print("Ascending order :", numbers)

elif choice == "d":
    numbers.sort(reverse=True)
    print("Descending order:", numbers)

else:
    print("Invalid choice. Please enter 'a' or 'd'.")