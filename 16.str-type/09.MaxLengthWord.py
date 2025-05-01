userInputString = input("Enter an string with multiple words: ")
maxLen = 0
maxLenWord = ""

for word in userInputString.split():
    if len(word) > maxLen:
        maxLen = len(word)
        maxLenWord = word

print("Maximum length word is:", maxLenWord)
