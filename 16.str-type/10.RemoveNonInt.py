# way-1

list = [1, 3.5, True, "Hello", "f", 69, "abc", "False", 6 + 9j]
newList = [intVal for intVal in list if type(intVal) == int]
print(newList)


# way-2

list = [1, 3.5, True, "Hello", "f", 69, "abc", "False", 6 + 9j]
index = len(list) - 1
while index >= 0:
    if type(list[index]) != int:
        del list[index]
    index -= 1

print(list)
