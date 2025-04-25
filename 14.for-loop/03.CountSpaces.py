s = input("Enter string: ")
count = 0
for val in s:
    if val == " ":
        count += 1

print("Number of spaces are: ", count)
