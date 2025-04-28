s = input("Enter an string: ")

for i in s:
    if i >= "a" and i <= "z" or i >= "A" and i <= "Z":
        pass
    else:
        print("String has atleast one character which is not alphabet")
        break
else:
    print("string has only alphabets in it")
