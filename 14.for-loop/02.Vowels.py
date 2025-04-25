s = input("Enter string: ")

## way-1

# for val in s:
#     if val == "a" or val == "e" or val == "i" or val == "o" or val == "u":
#         print(val)

## way-2

vowels = "aeiouAEIOU"
for val in s:
    if val in vowels:
        print(val)

print()
