first = {
    "name": "Bhoomika",
    "age": 19,
    "city": "Indore"
}

second = {
    "course": "Python",
    "language": "English",
    "city": "Bhopal"
}

merged = first.copy()
merged.update(second)

print("First Dictionary :", first)
print("Second Dictionary:", second)
print("\nMerged Dictionary :", merged)