userInputString = input("Enter a string: ")
list = userInputString.split(" ")

for i in list:
    print(i, end=",")

countWords = len(list)
print("Words count:", countWords)
print()

# Input: prince    bansal
# 	•	split(" ") splits at every single space, so extra empty strings get created!
# 	•	So you get:
# ['prince', '', '', '', 'bansal']

# ('' represents empty strings.)
# output:
# prince,,, ,bansal,
# Words count: 5


# way-2

# 	•	split() (without " ") automatically handles multiple spaces, tabs, etc.
#   •	It considers one or more whitespace as one separator.

countWords = len(input("Enter a string: ").split())
print("Words count:", countWords)
