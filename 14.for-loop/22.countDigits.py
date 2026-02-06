n = int(input("Enter a number: "))

# val = str(n)
# print("Number of digits:", len(val))

count=0
while n>0:
    # print(n)
    n = n//10
    count+=1
print("Number of digits:", count)

