userInputList = [
    int(element) for element in input("Enter comma separated values: ").split(",")
]
posList = []
nonPosList = []

for i in userInputList:
    if i > 0:
        posList.append(i)
    else:
        nonPosList.append(i)

print("Positive list:", posList, "\nNon positive list:", nonPosList)
