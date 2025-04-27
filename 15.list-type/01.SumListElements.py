l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sumAns = 0
for i in l:
    sumAns += i

print("Sum is:", sumAns)
print()

# way-2

print("Enter list numbers (separated by commas): ")
userInputList = [int(i) for i in input().split(",")]
sumOfValues = sum(userInputList)
print(userInputList, "=", sumOfValues)
