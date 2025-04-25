print("Enter coefficients a,b & c: ")
a, b, c = int(input()), int(input()), int(input())

if b * b == 4 * a * c:
    print("Roots are Real & Equal")
elif b * b > 4 * a * c:
    print("real & Distinct Roots")
else:
    print("Imaginary Roots")
