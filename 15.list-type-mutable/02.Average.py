l = [1, 90, 3, 4, 5, 6, 7, 8, 9, 10]
sumAns = 0
for i in l:
    sumAns += i
average = sumAns / len(l)
print("Average is:", average)
print()

# way-2

print("Enter list numbers (separated by commas): ")
userInputList = [int(i) for i in input().split(",")]
average = sum(userInputList) / len(userInputList)
print(userInputList, "=", average)
