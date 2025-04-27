l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listOfSquares = []

for i in l:
    square = i**2
    listOfSquares.append(square)
print("Squared list is:\n", listOfSquares)
print()

# way-2

print("Enter list numbers (separated by commas): ")
userInputList = [int(i) for i in input().split(",")]
ans = [element**2 for element in userInputList]
print("Squared list is:\n", ans)
