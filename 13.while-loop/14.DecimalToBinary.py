num = int(input("Enter n: "))

binaryString = ""

while num > 0:
    remainder = num % 2
    binaryString = str(remainder) + binaryString  # order of concatenation matters
    num //= 2

print("binary equivalent number:", binaryString)


# 10
# 10 % 2 = 0
# 10 // 2 = 5

# 5 % 2 = 1
# 5 // 2 = 2

# 2 % 2 = 0
# 2 // 2 = 1

# 1010
