list = ["AB", "BC", "CD", "BC", "AB", "DE"]
index = 0
for val in list:
    if list.index(val) != index:
        print("First repeated string is", val, "at index:", index)
        break
    index += 1
