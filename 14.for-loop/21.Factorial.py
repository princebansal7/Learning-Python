num = int(input("Enter N: "))
fact = 1

if num == 0 or num == 1:
    print("factorial is: 1")
else:
    for i in range(1, num + 1):
        fact = fact * i
    print("factorial is:", fact)

# n = 4
# 4! = 1 * 2 * 3 * 4 = 24
