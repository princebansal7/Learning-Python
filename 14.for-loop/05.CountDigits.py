s = input("Enter numeric string: ")
i, countUnique, countAllDigits = 0, 0, 0

for val in s:
    countAllDigits += 1
    if s.index(val) == i:
        countUnique += 1
    i += 1

print("All digits:", countAllDigits)
print("Unique digits:", countUnique)

print()
