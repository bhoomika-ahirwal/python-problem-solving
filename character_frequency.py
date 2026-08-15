text = input("Enter a string: ")

frequency = {}

for char in text.lower():
    if char != " ":
        frequency[char] = frequency.get(char, 0) + 1

print("\nCharacter Frequency")
print("-------------------")

for char, count in frequency.items():
    print(f"{char}: {count}")