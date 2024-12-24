print("Enter two numbers")
a, b = int(input()), int(input())

print("Before Swapping")
print("a =", a, "b =", b)

# way-1 (Python way)
a, b = b, a

print("After Swapping")
print("a =", a, "b =", b)

print()
# -------------------------------------

print("Before Swapping")
print("a =", a, "b =", b)

# way-2
temp = a
a = b
b = temp

print("After Swapping")
print("a =", a, "b =", b)
