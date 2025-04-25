num = int(input("Enter a number: "))

match num:
    case num if num > 0:
        print(num, "is Positive")
    case num if num < 0:
        print(num, "is Negative")
    case _:
        print(num, "is Zero")
