x = eval(input("Enter an number: "))
match x:
    case x if type(x) == int:
        print("int")
    case x if type(x) == float:
        print("float")
    case x if type(x) == bool:
        print("bool")
    case x if type(x) == complex:
        print("complex")
    case _:
        print("other data type")

print("outside match-block")
