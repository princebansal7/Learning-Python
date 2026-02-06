

n = int(input("Enter a number: "))

octal=""
while n>0:
    octal = str(n%8) + octal
    n//=8
print(octal)