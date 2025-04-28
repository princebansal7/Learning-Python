# '0' '1'  1   2   3   5   8   13   21   34 ...
#  f   s  f+s
#      f   s  f+s
#          f   s  f+s ....


n = int(input("Enter n: "))

firstTerm = 0
secondTerm = 1
fibonacciList = []

if n == 1:
    fibonacciList.append(firstTerm)
    print(fibonacciList)
elif n == 2:
    fibonacciList.append(firstTerm)
    fibonacciList.append(secondTerm)
    print(fibonacciList)
else:
    fibonacciList = [0, 1]
    loopIterateCount = 1
    while loopIterateCount <= n - 2:
        thirdTerm = firstTerm + secondTerm
        firstTerm = secondTerm
        secondTerm = thirdTerm
        loopIterateCount += 1
        fibonacciList.append(thirdTerm)
    print(fibonacciList)


# way-2

n = int(input("Enter n: "))

firstTerm = -1
secondTerm = 1
fibonacciList = []

while n:
    thirdTerm = firstTerm + secondTerm
    firstTerm = secondTerm
    secondTerm = thirdTerm
    fibonacciList.append(thirdTerm)
    n -= 1
print(fibonacciList)
