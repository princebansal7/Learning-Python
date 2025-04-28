userInputString = input("Enter a string: ")
vowelsCount = 0

for i in userInputString:
    if i in "aeiouAEIOU":
        vowelsCount += 1

print("Vowels count:", vowelsCount)
