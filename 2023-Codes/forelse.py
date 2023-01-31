val = input("Enter a string: ")

for i in val:
    if i == 'r':
        break
    print(i, end=" ")
else:
    print("All characters printed sucessfully")

print()
