a = 10


def f1():
    print("global var (a):", a)
    x = 20
    print("local var (x):", x)


f1()
print("global var (a):", a)
# print("local var (x):", x)  # Error as x only exists in f1 body


#######################
# str = "abcdddd"
# for x in str:
#     if(x=="r"):
#         break
#     print(x)
# else:
#     print("end")


# x, y, z = int(input()), int(input()), int(input())
# print(x, y, z)

# i = 1
# isEven = False
# while i <= 3:
#     num = int(input(f"Enter even number: (Try-{i}): "))
#     if num % 2 == 0:
#         print("Winner")
#         isEven = True
#         break
#     i += 1

# if isEven == False:
#     print("Loser")


# i = 1
# while i <= 10:
#     if i % 2 == 0:
#         i += 1
#         continue
#     print(i)
#     i += 1


# a = 0
# for b in range(0, 10, 2):
#     a = a + b + 1

# print(a)


# def function_a(n):
#     if n == 0:
#         return 1
#     else:
#         return n * function_b(n - 1)


# def function_b(n):
#     if n == 0:
#         return 1
#     else:
#         return n * function_a(n - 1)


# print(function_a(4))


def f(**d):
    for k, v in d.items():
        print(k, ":", v)


f(name="Prince", age=20)
f(name="Naruto", age=20, marks=30)
f(name="Ramesh", age=20, emp_id="10b7")
