n = int(input("Enter n: "))

primeNumList = []

for val in range(2, n + 1):
    for i in range(2, val):
        if val % i == 0:
            break
    else:
        primeNumList.append(val)

print("Prime numbers till", n, "are:\n", primeNumList)
print()

# First N prime numbers:

# n=10
# [2,3,5,7,11,13,17,19,23,29]

n = int(input("Enter n: "))
temp = n
primeNumList = []
startPrime = 2
while n:
    for i in range(2, startPrime):
        if startPrime % i == 0:
            break
    else:
        primeNumList.append(startPrime)
        n -= 1
    startPrime += 1

print("First", temp, "Prime numbers are:\n", primeNumList)
