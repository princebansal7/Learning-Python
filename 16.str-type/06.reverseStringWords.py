# "prince bansal" is a given string and resulting string should be "bansal prince")

# 1 way-1

userInputString = input("Enter a string: ")
list = [element for element in userInputString.split(" ")]

reversedList = []
for i in list[::-1]:
    reversedList.append(i)

print(reversedList)

# 2 Another way

reversedList = " ".join(input("Enter a string: ").split(" ")[::-1])
print(reversedList)

# ----------------------------
# 3 reverse individual words?
# input: prince bansal
# output: ecnirp lasnab

userInputString = input("Enter a string: ")
list = [element for element in userInputString.split(" ")]

reverseWordList = []
for i in list:
    i = i[::-1]
    reverseWordList.append(i)

print(reverseWordList)
