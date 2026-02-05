# set comprehension
userInput = {int(e) for e in input("Enter comma seperated values: ").split(",")}
print(userInput)

# set comprehension
odd = {val for val in userInput if val % 2 == 1}
print("Odd values:", set(odd))

# converting list into set later
even = [val for val in userInput if val % 2 == 0]
print("Even values:", set(even))


## Shorter Solution

userInput = {int(e) for e in input("Enter comma seperated values: ").split(",")}
print(userInput)

odd = set()
even = set()
for val in userInput:
    if val % 2 == 1:
        odd.add(val)
    else:
        even.add(val)

print("Odd values:", odd)
print("Even values:", even)
