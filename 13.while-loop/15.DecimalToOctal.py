num = int(input("Enter n: "))

octalString = ""

while num > 0:
    remainder = num % 8
    octalString = str(remainder) + octalString  # order of concatenation matters
    num //= 8

print("octal equivalent number:", octalString)


# 100
# 100 % 8 = 4
# 100 // 8 = 12

# 12 % 8 = 4
# 12 // 8 = 1 (end)

# 144
