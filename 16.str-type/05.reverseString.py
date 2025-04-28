# userInputString = input("Enter a string: ")
# i, j = 0, len(userInputString) - 1
# while i < j:
#     temp = userInputString[i]
#     userInputString[i] = userInputString[j]
#     userInputString[j] = temp
#     i += 1
#     j -= 1

# print(userInputString)
# above solution won't work as str is immutable


# Python way - use Slicing

userInputString = input("Enter a string: ")
reversedString = userInputString[::-1]
print(reversedString)
