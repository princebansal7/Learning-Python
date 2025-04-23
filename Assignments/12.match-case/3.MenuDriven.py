while True:
    print()
    print("1.Odd-Even")
    print("2.Positive or Non-Positive")
    print("3.Simple Interest")
    print("4.Find Roots of Quadratic equation")
    print("5.EXIT")
    print()
    choice = int(input("Enter Choice: "))
    match choice:
        case 1:
            print()
            num = int(input("Enter a number: "))
            if num & 1:
                print("Odd Number")
            else:
                print("Even Number")
            print()
        case 2:
            print()
            num = int(input("Enter a number: "))
            if num > 0:
                print("Positive number")
            else:
                print("Non Positive number")
            print()
        case 3:
            print()
            p = int(input("Enter principle: "))
            r = int(input("Enter rate of interest: "))
            t = int(input("Enter time period: "))
            simpleInterest = (p * r * t) / 100
            print()
            print("Simple Interest is: ", simpleInterest)
            print()
        case 4:
            print()
            print("Ax^2 + Bx + C = 0")
            print("Enter coefficients A,B & C: ")
            a, b, c = int(input()), int(input()), int(input())
            d = (b * b) - (4 * a * c)
            root1 = (-b + (d ** (1 / 2))) / 2 * a
            root2 = (-b - (d ** (1 / 2))) / 2 * a
            print()
            print("root1 = ", f"{root1:.2f}", "\n", "root2 = ", f"{root2:.2f}")
            print()
        case 5:
            break
        case _:
            print()
            print("Invalid Choice")
            print()
