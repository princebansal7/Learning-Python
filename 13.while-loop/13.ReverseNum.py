num = int(input("Enter +ve n: "))
reverse = 0

while num > 0:
    lastDigit = num % 10
    reverse = reverse * 10 + lastDigit
    num //= 10

print("Reversed number:", reverse)


# 123
# 3*10^2 + 2*10^1 + 1*10^1 => 321
