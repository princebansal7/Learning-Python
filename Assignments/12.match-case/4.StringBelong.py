myString = input("Enter any part of the string (Prince Bansal): ")

match myString:
    case myString if myString in "Prince":
        print("Belongs to First Name")
    case myString if myString in "Bansal":
        print("Belongs to Last Name")
    case _:
        print("Does not belong to asked string")

print()
print("Outside match-case block")
