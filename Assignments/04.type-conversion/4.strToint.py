
val1 = '10'
print(val1, type(val1))


val2 = int(val1)
print(val2, type(val2))

# NOTE: When string is purely integer only then we can convert it to int

a = '10a'
b = '23.69'
print(int(a), type(a))  # will given error
print(int(b), type(b))  # will given error
