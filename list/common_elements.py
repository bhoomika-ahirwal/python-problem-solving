first = list(map(int, input("Enter first list: ").split()))
second = list(map(int, input("Enter second list: ").split()))

common = []

for number in first:
    if number in second and number not in common:
        common.append(number)

print("First list  :", first)
print("Second list :", second)
print("Common      :", common)