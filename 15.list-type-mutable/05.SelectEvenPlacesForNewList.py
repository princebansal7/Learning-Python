print("Enter list numbers (separated by commas): ")
list = [int(i) for i in input().split(",")]

evenPlacedElementsList = []
i = 1
while i < len(list):
    evenPlacedElementsList.append(list[i])
    i += 2
print(evenPlacedElementsList)
print()

# way-2

ans = [i for i in list if list.index(i) % 2 == 1]
print(ans)


# 1st pos   2nd pos   3rd pos   4th pos
#    1,        2,        3,       4
# => even position elements = [2,4]
