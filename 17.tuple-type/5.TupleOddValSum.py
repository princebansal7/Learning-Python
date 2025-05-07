t = (1, 2, 3, 4, 67, 9, 23, 10)
print(t)
sum = 0
for i in t:
    if i % 2 == 1:
        sum += i

print("Sum of odd values:", sum)
