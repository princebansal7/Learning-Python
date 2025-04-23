x = int(input("Enter a number: "))
match x:
    case x if x > 99 and x <= 999:
        print("3 digit number")
    case _:
        print("Not a 3 digit number")
