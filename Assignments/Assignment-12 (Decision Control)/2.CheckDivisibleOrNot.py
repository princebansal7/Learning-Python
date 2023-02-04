num = int(input("Enter number: "))

if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not Divisible")


# Way-2
print("Divisible by 5" if num % 5 == 0 else "Not Divisible")
