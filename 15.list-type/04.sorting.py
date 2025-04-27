print("Enter list numbers (separated by commas): ")
userInputList = [int(i) for i in input().split(",")]

print("Sorting is Descending order:")
userInputList.sort(reverse=True)
print(userInputList)
print()


print("Sorting is Ascending order:")
userInputList.sort()
print(userInputList)
print()
