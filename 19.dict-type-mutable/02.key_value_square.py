n = int(input("Enter number: "))
d={}
for i in range(1,n+1):
    d[i]=i**2

for key, value in d.items():
    print(key,"->",value)

print(d)