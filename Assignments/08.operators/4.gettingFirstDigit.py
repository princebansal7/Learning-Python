num = int(input("Enter a 3 digit number: "))
withoutLastDigit = num//10  # floor integer division
withoutLastDigit = withoutLastDigit//10  # floor integer division
print("First digit is:", withoutLastDigit)
