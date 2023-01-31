
# for i in range(1, 6):
#     print('prince', i)

# print()

# a = 0
# while a < 5:
#     print("Hello", a)
#     a += 2


chance = 1
while chance <= 3:
    num = int(input("Enter a even number: "))
    if num % 2 == 0:
        break
    chance += 1

if chance == 4:
    print("you lose")
else:
    print("You WOn")
