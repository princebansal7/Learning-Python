n = int(input("Enter a number: "))
sum=0
while n>0:
    lastDigit = n%10
    sum = sum + lastDigit
    n = n//10
    
print("Sum of digits:", sum)

