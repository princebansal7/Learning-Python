print("Enter 9 values (row wise) for 3X3 matrix")
m1 = [
    [int(element) for element in input().split(",")],
    [int(element) for element in input().split(",")],
    [int(element) for element in input().split(",")],
]

print("Enter 9 values (row wise) for 3X3 matrix")
m2 = [
    [int(element) for element in input().split(",")],
    [int(element) for element in input().split(",")],
    [int(element) for element in input().split(",")],
]

sumMatrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

print("Sum of matrix m1, m2 is: ")
for i in range(0, 3):
    for j in range(0, 3):
        sumMatrix[i][j] = m1[i][j] + m2[i][j]
        print(sumMatrix[i][j], end=" ")
    print()

# Enter 9 values (row wise) for 3X3 matrix
# 1,2,3
# 4,5,6
# 7,8,9
# Enter 9 values (row wise) for 3X3 matrix
# 11,12,13
# 14,15,16
# 17,18,19
# Sum of matrix m1, m2 is:
# 12 14 16
# 18 20 22
# 24 26 28
