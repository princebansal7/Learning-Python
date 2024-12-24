num = int(input("Enter a 3 digit number: "))
withoutLastDigit = num//10  # floor integer division
lastDigit = withoutLastDigit % 10  # floor integer division
print("Middle digit is:", lastDigit)
