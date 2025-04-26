start = int(input("Enter start value: "))
end = int(input("Enter end value: "))

# for val in range(start, end + 1):
#     countDivisor = 0
#     for i in range(1, val + 1):
#         if val % i == 0:
#             countDivisor += 1
#     if countDivisor == 2:
#         print(val, end=" ")


for val in range(start, end + 1):
    for i in range(2, val):
        if val % i == 0:
            break
    else:
        print(val, end=" ")

print()
