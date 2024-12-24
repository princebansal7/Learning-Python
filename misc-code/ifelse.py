x = int(input("Enter marks: "))
if x > 90 and x <= 100:
    print("A Grade")
elif x > 80 and x <= 90:
    print("B Grade")
elif x > 70 and x <= 80:
    print("C Grade")
elif x > 60 and x <= 70:
    print("D Grade")
elif x > 50 and x <= 60:
    print("E Grade")
else:
    print("F")

# single line if-else

value = "true" if 69 > 0 else "false"
print(value)
