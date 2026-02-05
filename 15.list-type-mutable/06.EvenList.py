n = int(input("Enter n: "))
evenNElementsList = []
for i in range(1, n + 1):
    evenNElementsList.append(2 * i)
print(evenNElementsList)

# way-2

ans = [2 * i for i in range(1, n + 1)]
print(ans)
