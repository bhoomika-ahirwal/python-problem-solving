text = input("Enter a word or number: ")

cleaned_text = text.replace(" ", "").lower()

if cleaned_text == cleaned_text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")