list = [10, 20, 10, 10, 20, 30, 20, 10, 20, 10, 20, 20, 30]
index = 0

for val in list:
    if index == list.index(val):
        print(val, "==>", list.count(val))
    index += 1
