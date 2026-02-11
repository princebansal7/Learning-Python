d = {
    1:"value1",
    4:"vallue4",
    7:"value7",
    69:"value69",
    5:"value5"
}

print(sorted(d,reverse=True)) # will return sorted keys list: [69, 7, 5, 4, 1] => wrong
print()
sorted_dict = { k:d[k] for k in sorted(d,reverse=True)}
print(sorted_dict)
