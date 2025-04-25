s = input("Enter numeric string: ")
i = 0
for val in s:
    if s.index(val) == i:
        print(val, end="")
    i += 1

print()


# "1122345677" -> "1234567"
