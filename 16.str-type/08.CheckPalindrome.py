userInputString = input("Enter an string: ")
temp = userInputString

reversedString = userInputString[::-1]

if userInputString == reversedString:
    print("Palindrome")
else:
    print("Not Palindrome")


## Shorter way:------------

print("Palindrome" if userInputString == userInputString[::-1] else "Not Palindrome")

###-----------------------
print()
print("user string in uppercase: ", end=" ")
print(userInputString.upper())
print("check if user string is uppercase: ", end=" ")
print(userInputString.isupper())
print("check if user string is lowercare: ", end=" ")
print(userInputString.lower())
print("user string in lowercare: ", end=" ")
print(userInputString.islower())
print()

# input: "madam"
# output: Palindrome

# input: "damad"
# output: Palindrome

# input: "racecar"
# output: Palindrome

# input: "madame"
# output: Not Palindrome
