givenListOfStrings = ["prince", "prem", "radha", "raja", "pal"]
tempList = []
for val in givenListOfStrings:
    if val.startswith("p"):
        tempList.append(val)
ans = tuple(tempList)
print(ans)

# will return a tuple of strings starting with 'p'
# ("prince", "prem", "pal")


# We want like:  # [("prince", "prem", "pal"),("radha","raja")] => list of tuples of strings
# string with same character


givenListOfStrings = ["prince", "prem", "radha", "raja", "lama", "lowe"]
alphabets = "abcdefghijklmnopqrstuvwxyz"
tempList = []
ans = []
givenListOfStrings.sort()

for i in range(0, 26):
    tempList.clear()
    for val in givenListOfStrings:
        if val.startswith(alphabets[i]):
            tempList.append(val)
    if len(tempList) > 0:
        ans.append(tuple(tempList))
print(ans)
