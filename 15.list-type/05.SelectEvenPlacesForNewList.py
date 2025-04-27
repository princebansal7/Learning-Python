list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenPlacedElementsList = []
i = 1
while i < len(list):
    evenPlacedElementsList.append(list[i])
    i += 2
print(evenPlacedElementsList)


# way-2

ans = [i for i in list if list.index(i) % 2 == 1]
print(ans)
