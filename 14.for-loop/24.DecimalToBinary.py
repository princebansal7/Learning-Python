

n = int(input("Enter a number: "))
# carryList = []
# while n>0:
#     carry = n%2
#     carryList.append(carry)
#     n=n//2

# print(carryList)
# binaryList = carryList[::-1]
# print(binaryList)

# finalBianry = ""
# for i in binaryList:
#     finalBianry+=str(i)

# print("final Binary: ",finalBianry)


## way-2

binary=""
while n>0:
    binary = str(n%2) + binary
    n//=2
print(binary)



