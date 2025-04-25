i = 10
while i >= 1:
    print(2 * i, end=" ")
    i -= 1
print()

# with user input

num = int(input("Enter N: "))
print("printing first N even numbers in reverse order")
while num > 0:
    print(2 * num, end=" ")
    num -= 1
print()
