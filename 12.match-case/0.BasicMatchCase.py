x = eval(input("Enter any of (1, 2, 3.4, True, bool, 3+4j): "))
match x:
    case 1:
        print("int")
    case 2:
        print("int")
    case 3.4:
        print("float")
    case True:
        print("bool")
    case 3 + 4j:
        print("complex")
    case _:
        print("string or invalid")

print("outside match-block")
