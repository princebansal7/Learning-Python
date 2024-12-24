print("Enter Three numbers a,b & c: ")
a, b, c = int(input()), int(input()), int(input())

if a > b:
    if a > c:
        print("a:", a)
    else:
        print("c:", c)
else:
    if b > c:
        print("b:", b)
    else:
        print("c:", c)
