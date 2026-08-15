first = input("Enter first word: ")
second = input("Enter second word: ")

first = first.replace(" ", "").lower()
second = second.replace(" ", "").lower()

if sorted(first) == sorted(second):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")