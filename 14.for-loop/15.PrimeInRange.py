start = 15
end = 45
for val in range(start, end + 1):
    countDivisor = 0
    for i in range(1, val + 1):
        if val % i == 0:
            countDivisor += 1
    if countDivisor == 2:
        print(val, end=" ")

print()
