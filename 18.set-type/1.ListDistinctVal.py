list = [int(e) for e in input("Enter comma seperated values: ").split(",")]
print(list)
ans = [val for val in set(list)]
print("Distinct values: ", ans)
