num = eval(input("Enter value: "))

# match & case are soft keywords: they behave like keywords but we can use them as variable name too

match num:
    case 1.2:
        print("Float value")
    case 69:
        print("int value")
    case "Prince":
        print("String value")
    case True:
        print("Boolean value")
    case 6+9j:
        print("Complex value")
    case 69:
        print("Duplicate case")  # duplicate case: only first match will work
    case _:
        print("Default case: INVALID")


print("Outside match")

# no error
match = "prince"
print(match)
