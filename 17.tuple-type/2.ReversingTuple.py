t = tuple(
    [int(val) for val in input("Enter int values separated by commas: ").split(",")]
)
print("Tuple: ", t)

reversedTuple = t[::-1]
print("Revered tuple: ", reversedTuple)
