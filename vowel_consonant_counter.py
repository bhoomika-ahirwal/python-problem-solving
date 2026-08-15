text = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
special_characters = 0

for char in text.lower():

    if char in "aeiou":
        vowels += 1

    elif char.isalpha():
        consonants += 1

    elif char.isdigit():
        digits += 1

    elif not char.isspace():
        special_characters += 1

print("\nCharacter Analysis")
print("------------------")
print("Vowels             :", vowels)
print("Consonants         :", consonants)
print("Digits             :", digits)
print("Special Characters :", special_characters)