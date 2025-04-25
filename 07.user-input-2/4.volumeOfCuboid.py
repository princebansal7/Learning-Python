l = int(input("Enter length: "))
b = int(input("Enter breadth: "))
h = int(input("Enter height: "))

volume = l * b * h

if l == b and b == h:
    print("Volume of Cube is:", volume)
else:
    print("Volume of Cuboid is:", volume)
