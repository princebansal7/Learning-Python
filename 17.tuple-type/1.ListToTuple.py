t1 = tuple([1, 2, 3, 4, 5, 6])
print(t1[1])  # 2


t2 = (10, 20, True, "prince", [1, 2, 3, 4], 3.4, 9 + 10j)
# t2[4] = 69  # Error - can't modify immutable object value

# But we can modify the tuple's element element's value if the element itself is mutable
t2[4][2] = 69
print(t2)


# user input in tuple
t3 = tuple(
    [int(val) for val in input("Enter int values separated by commas: ").split(",")]
)
print(t3)
