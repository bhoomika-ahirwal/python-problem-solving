text = input("Enter a sentence: ")

words = text.split()
characters = len(text)
spaces = text.count(" ")

print("\nText Analysis")
print("-------------")
print("Words      :", len(words))
print("Characters :", characters)
print("Spaces     :", spaces)