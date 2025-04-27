l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listOfSquares = []

for i in l:
    square = i**2
    listOfSquares.append(square)
print("Squared list is:\n", listOfSquares)


# way-2

ans = [element**2 for element in l]
print("Squared list is:\n", ans)
