elements = (
    f"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+|><?/"
)
ans = []
for i in elements:
    tempTuple = (i, ord(i))
    ans.append(tempTuple)

print(ans)

# output
# [('a', 97), ('b', 98), ('c', 99), ('d', 100),...]
