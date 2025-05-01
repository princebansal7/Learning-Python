userInputString = input("Enter an alphanumeric string: ")
ans = []
for i in userInputString:
    if i.isdigit():
        ans.append(int(i))
print(ans)

# input: a1bce23b4nnm3
# output: [1,2,3,4,3]
